import numpy as np
from tenbagger.src.passiveIncome.calculator import PassiveIncomeCalculator
import pandas as pd


class PassiveDividends(PassiveIncomeCalculator):
    def __init__(self, port):
        super().__init__(port=port)

    def calulate_dividends(self, n: int, growth_stock, growth_dividend, monthly_payment, method='proportional',
                           only_dividend_stocks=False, generate_report: bool = False):
        """

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

        yearly_div = 0
        for m in range(0, n + 1):

            month = (m % 12) + 1
            df['adding_shares'] = (df['percentage'] * monthly_payment) / df['price']

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
                    'staking_rewards': [None],
                    'portfolio_value': [df.value.sum()],
                    'growth_stock': [growth_stock],
                    'dividend_growth': [growth_dividend]}
            self.df_report = pd.concat([self.df_report, pd.DataFrame.from_dict(data)], axis=0)

            if month == 12:
                self.payout['Dividends'] = self.payout['Dividends'] * rate_dividend
                print(f'Yearly divdend: {yearly_div}')
                df['price'] *= rate
                yearly_div = 0  # reset

        yearly_div = np.sum(df.price * df.amount * df['yield'])
        print(f'Yearly divdend: {yearly_div}')

        # write report
        if generate_report:
            self.generate_report(method=method)

        return df

    pass

