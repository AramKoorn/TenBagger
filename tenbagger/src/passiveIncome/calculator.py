from tenbagger.src.portfolio.core import Portfolio
from tenbagger.src.utils.utilities import read_yaml
from tenbagger.src.dividends.div import Dividends
import numpy as np
import pandas as pd
from tqdm import tqdm
import os


class DividendCalculator:
    def __init__(self, port):
        self.port = read_yaml('configs/portfolio.yaml')[port]

        self.dist = Portfolio(port)
        self.dist.unification()

        res = []
        for ticker in tqdm(self.port):
            div = Dividends(ticker)
            if div.df.shape[0] != 0:
                projected = div.projected_dividends()
                projected['ticker'] = ticker
                projected = projected[['ticker', 'Dividends', 'month']]
                res.append(projected)

        self.res = pd.concat(res)
        self.payout = pd.concat({month: self.res.query(f'month == {month}') for month in set(self.res.month)}).reset_index(drop=True)

    def calulate_dividends(self, n: int, growth_stock, growth_dividend, monthly_payment, method='proportional', only_dividend_stocks=False,
                           generate_report: bool = False):
        """

        :param n: number of months
        :return:
        """

        df_report = pd.DataFrame()

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
        df['adding_shares'] = (df['percentage'] * monthly_payment) / df['price']

        yearly_div = 0
        for m in range(0, n + 1):

            month = (m % 12) + 1

            # add the dividends
            tmp = self.payout[self.payout.month == month].copy()
            df['monthly_dividend'] = 0
            df['dripping'] = 0
            for ticker in set(tmp.ticker):

                amount = df.loc[df.ticker == ticker, 'amount'].values[0]
                div = tmp.loc[tmp.ticker == ticker, 'Dividends'].values[0]
                df.loc[df.ticker == ticker, 'monthly_dividend'] = amount * div

            df['dripping'] = np.where(df.monthly_dividend > 0, df.monthly_dividend / df.price, 0)
            df['amount'] += df['adding_shares'] + df['dripping']
            yearly_div += df['monthly_dividend'].sum()
            df['value'] = df.amount * df.price

            data = {'month': [m],
                    'paid_dividends': [df.monthly_dividend.sum()],
                    'portfolio_value': [df.value.sum()],
                    'growth_stock': [growth_stock],
                    'dividend_growth': [growth_dividend]}
            df_report = pd.concat([df_report, pd.DataFrame.from_dict(data)], axis=0)

            if month == 12:
                self.payout['Dividends'] = self.payout['Dividends'] * rate_dividend
                print(f'Yearly divdend: {yearly_div}')
                df['price'] *= rate
                yearly_div = 0  # reset

        yearly_div = np.sum(df.price * df.amount * df['yield'])
        print(f'Yearly divdend: {yearly_div}')

        if generate_report:
            date = pd.to_datetime('now')
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

            df_report.to_csv(path + '/' + file_name)

        return df