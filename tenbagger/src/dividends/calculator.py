from tenbagger.src.scripts.portfolio import Portfolio
from tenbagger.src.utils.utilities import read_yaml
from tenbagger.src.dividends.div import Dividends
import numpy as np
from tqdm import tqdm


class DividendCalculator:
    def __init__(self, port):
        self.port = read_yaml('user_data/portfolio/portfolio.yaml')[port]

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
        self.payout = {month: self.res.query(f'month == {month}') for month in set(self.res.month)}

    def calulate_dividends(self, n, growth, monthly_payment, only_dividend_stocks=False):
        """

        :param n: number of months
        :return:
        """

        df = self.dist.df.copy()
        rate = 1 + growth

        if growth < 0 or growth > 1:
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
            tmp = self.payout[month]
            df['monthly_dividend'] = 0
            df['dripping'] = 0
            for ticker in set(tmp.ticker):

                amount = df.loc[df.ticker == ticker, 'amount'].values[0]
                div = tmp.loc[tmp.ticker == ticker, 'Dividends'].values[0]
                df.loc[df.ticker == ticker, 'monthly_dividend'] = amount * div

            df['dripping'] = np.where(df.monthly_dividend > 0, df.monthly_dividend / df.price, 0)
            df['amount'] += df['adding_shares'] + df['dripping']
            yearly_div += df['monthly_dividend'].sum()

            if month == 12:
                print(f'Yearly divdend: {yearly_div}')
                df['price'] *= rate
                yearly_div = 0  # reset

        yearly_div = np.sum(df.price * df.amount * df['yield'])
        print(f'Yearly divdend: {yearly_div}')

        return df

if __name__ == "__main__":
    import pandas as pd
    pd.set_option('expand_frame_repr', False)

    d = DividendCalculator(port='aram')
    d.calulate_dividends(n=120, growth=0, monthly_payment=1200, only_dividend_stocks=True)
