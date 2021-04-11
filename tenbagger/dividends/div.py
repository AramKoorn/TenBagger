import pandas as pd
import numpy as np
from tenbagger.scripts.utilities import Ticker, Converter, read_yaml
import datetime
from tqdm import tqdm


class Dividends:
    def __init__(self, ticker):
        self.ticker = ticker
        self.env = read_yaml('configs/environment.yaml')

        try:
            self.df = self._clean()
        except:
            self.df = None

    def request(self):
        return pd.read_html(
            f'https://finance.yahoo.com/quote/{self.ticker}/history?period1=1460332800&period2=1618099200&interval=div%7Csplit&filter=div&frequency=1d&includeAdjustedClose=true')[0]

    def _clean(self):
        df = self.request()
        df = df[:-1]

        # We only need these 2 columns
        df = df[['Date', 'Dividends']]

        # Make it a datetime column
        df['Date'] = pd.to_datetime(df['Date'])
        df['Dividends'] = np.float32(df['Dividends'].apply(lambda x: x.replace('Dividend', "")))

        # Convert to correct currency
        df['currency'] = Ticker(self.ticker).get_currency()
        Converter(df)._convert(currency=self.env['CURRENCY'], col_ind='currency', col_currency='Dividends')

        return df

    def projected_dividends(self):
        this_year = pd.Timestamp.now().year
        prev_year = this_year - 1

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
        df['month'] = df.month.apply(lambda x: datetime.date(1900, x, 1).strftime('%B'))
        df = df[['level_0', "Dividends", 'Date', 'month', 'year']].rename(columns={'level_0': 'ticker'}).copy()

        return df


if __name__ == '__main__':

    pd.set_option("expand_frame_repr", False)
    port = read_yaml('configs/portfolio.yaml')

    d = DividendsPortfolio(port['aram'])
    d.calculate()

    d = Dividends('ibm')
    d._clean()
    d.df
    x = 2
