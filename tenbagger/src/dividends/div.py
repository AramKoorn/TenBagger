import pandas as pd

from tenbagger.src.utils.utilities import Ticker, read_yaml
import datetime
from tqdm import tqdm
from currency_converter import CurrencyConverter


class Dividends:
    def __init__(self, ticker):
        self.ticker = ticker
        self.env = read_yaml('user_data/env/environment.yaml')

        try:
            self.df = self._clean()
        except:
            self.df = None

    def request(self):

        df = Ticker(self.ticker).ticker.actions.tail(10).reset_index()

        return df

    def _clean(self):

        df = self.request()

        # We only need these 2 columns
        df = df[['Date', 'Dividends']]

        # Convert to correct currency
        df['currency'] = Ticker(self.ticker).get_currency()
        c = CurrencyConverter()
        df['Dividends'] = df.apply(lambda x: c.convert(x.Dividends, x.currency, self.env["CURRENCY"]), axis=1)
        df['currency'] = self.env["CURRENCY"]

        return df

    def projected_dividends(self):
        this_year = pd.Timestamp.now().year
        prev_year = this_year - 1

        # Last payout
        last_div = self.df.Dividends[0]

        # Get year
        df = self.df.copy()
        df['year'] = self.df.Date.apply(lambda x: x.year)
        df = df.query('year == @prev_year').copy()
        df['month'] = df.Date.apply(lambda x: x.month)

        # Projected dividends
        df['year'] = df['year'] + 1
        df['Dividends'] = last_div

        return df


class DividendsPortfolio:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def calculate(self):

        res = {}
        for ticker, amount in tqdm(self.portfolio.items()):
            div = Dividends(ticker)
            if div.df.shape[0] != 0:
                df = div.projected_dividends()
                df['Dividends'] = df.Dividends * amount
                res[ticker] = df

        df = pd.concat(res).reset_index()
        df = df.sort_values("month")
        df['month'] = df.month.apply(lambda x: datetime.date(1900, x, 1).strftime('%B'))
        df = df[['level_0', "Dividends", 'Date', 'month', 'year']].rename(columns={'level_0': 'ticker'}).copy()

        return df


if __name__ == '__main__':

    pd.set_option("expand_frame_repr", False)
    port = read_yaml('user_data/portfolio/portfolio.yaml')

    d = DividendsPortfolio(port['test_calculator'])
    d.calculate()

    d = Dividends('ibm')
    d._clean()
    d.df
    d.projected_dividends()