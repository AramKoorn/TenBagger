from tenbagger.src.portfolio.core import Portfolio
from tenbagger.src.utils.utilities import read_yaml
from tenbagger.src.dividends.div import Dividends
import numpy as np
import pandas as pd
from tqdm import tqdm
import os


class PassiveIncomeCalculator:
    def __init__(self, port):
        if isinstance(port, str):
            self.port = read_yaml('user_data/portfolio/portfolio.yaml')[port]
        else:
            self.port = port

        self.dist = Portfolio(port)
        self.dist.unification()
        self.df_report = pd.DataFrame()

        res = []
        for ticker in tqdm(self.port):
            div = Dividends(ticker)
            if div.df is not None:
                if div.df.shape[0] != 0:
                    projected = div.projected_dividends()
                    projected['ticker'] = ticker
                    projected = projected[['ticker', 'Dividends', 'month']]
                    res.append(projected)

        self.res = pd.concat(res)
        self.payout = pd.concat(
            {month: self.res.query(f'month == {month}') for month in set(self.res.month)}).reset_index(drop=True)

        self.crypto = self.dist.df.query('type == "CRYPTOCURRENCY"').copy()
        self.crypto_payout = pd.DataFrame()

        # For now we only look at monthly crypto rewards
        for token in set(self.crypto.ticker):
            monthly_payout = ((self.crypto.loc[self.crypto.ticker == token, 'apy'].values[0] ) * self.crypto.loc[self.crypto.ticker == token, 'price'].values[0]) / 12
            range_months = list(range(1, 13))
            crypto_payout = {'ticker': [token] * 12, 'staking_rewards': [monthly_payout] * 12, 'month': range_months}
            df_tmp = pd.DataFrame(crypto_payout).copy()
            self.crypto_payout = pd.concat([self.crypto_payout, df_tmp])

    def calulate(self, n: int, growth_stock, growth_dividend, monthly_payment, method='proportional',
                           only_dividend_stocks=False, generate_report: bool = False):
        """
        Calculator passive income for a given portfolio and method

        :param n: number of months
        :return:
        """

        df = self.dist.df.copy()
        rate = 1 + growth_stock
        rate_dividend = 1 + growth_dividend

        if growth_stock < 0 or growth_stock > 1:
            raise ValueError("Growth should ben between [0, 1]")

        if only_dividend_stocks:
            df = df[df['yield'].notna()].copy()
            df['percentage'] = df['value'].apply(lambda x: x / sum(df['value']))
        else:
            df['percentage'] = np.float32(df['percentage'].apply(lambda x: x.replace('%', ''))) / 100
        df['monthly'] = monthly_payment

        yearly_div, yearly_staking = 0, 0
        for m in range(0, n + 1):

            month = (m % 12) + 1
            df['adding_units'] = (df['percentage'] * monthly_payment) / df['price']

            # add the dividends
            tmp = self.payout[self.payout.month == month].copy()
            df['monthly_dividend'] = 0
            df['dripping'] = 0
            for ticker in set(tmp.ticker):

                # If stonk
                amount = df.loc[df.ticker == ticker, 'amount'].values[0]
                div = tmp.loc[tmp.ticker == ticker, 'Dividends'].values[0]
                df.loc[df.ticker == ticker, 'monthly_dividend'] = amount * div

            tmp = self.crypto_payout[self.crypto_payout.month == month].copy()
            for ticker in set(self.crypto_payout.ticker):
                if not only_dividend_stocks:
                    amount = df.loc[df.ticker == ticker, 'amount'].values[0]
                    sr = (df.loc[df.ticker == ticker, 'apy'].values[0] * df.loc[df.ticker == ticker, 'price'].values[0]) / 12
                    df.loc[df.ticker == ticker, 'monthly_staking_rewards'] = amount * sr
                else:
                    df['monthly_staking_rewards'] = 0

            df['dripping'] = np.where(df.monthly_dividend > 0, df.monthly_dividend / df.price, 0)
            df['drip_staking_rewards'] = np.where(df.monthly_staking_rewards > 0, df.monthly_staking_rewards / df.price, 0)
            df['amount'] += df['adding_units'] + df['dripping'] + df['drip_staking_rewards']
            yearly_div += df['monthly_dividend'].sum()
            yearly_staking += df['drip_staking_rewards'].sum()
            df['value'] = df.amount * df.price

            data = {'month': [m],
                    'paid_dividends': [df.monthly_dividend.sum()],
                    'staking_rewards': [df.monthly_staking_rewards.sum()],
                    'total_passive_income': [df.monthly_dividend.sum() + df.monthly_staking_rewards.sum()],
                    'portfolio_value': [df.value.sum()],
                    'growth_stock': [growth_stock],
                    'dividend_growth': [growth_dividend]}
            self.df_report = pd.concat([self.df_report, pd.DataFrame.from_dict(data)], axis=0)

            if month == 12:
                self.payout['Dividends'] = self.payout['Dividends'] * rate_dividend
                print(f'Yearly divdend: {yearly_div}')
                df['price'] *= rate
                yearly_div = 0  # reset
                yearly_staking = 0

        yearly_div = np.sum(df.price * df.amount * df['yield'])
        yearly_staking_rewards = np.sum(df.price * df.amount * df['apy'])
        print(f'Yearly divdend: {yearly_div}')
        print(f'Yearly staking rewards: {yearly_staking_rewards}')

        # write report
        if generate_report:
            self.generate_report(method=method)

        return df

    def generate_report(self, method):

        file_name = f'method: {method}.csv'

        # set directory
        path = os.getcwd() + '/data/'

        # Create data directory if not exist already
        if not os.path.exists(path):
            os.mkdir(path)

        path = path + "/" + str(pd.to_datetime('today'))

        # Create data directory if not exist already
        if not os.path.exists(path):
            os.mkdir(path)

        self.df_report.to_csv(path + '/' + file_name)


if __name__ == '__main__':
    c = PassiveIncomeCalculator('aram')
    c.calulate(n=120, growth_stock=0.03, growth_dividend=0.03, monthly_payment=1000,
                            generate_report=True, only_dividend_stocks=False)
