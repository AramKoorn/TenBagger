from tenbagger.scripts.utilities import read_yaml, Ticker, Converter, make_percentage
import yfinance as yf
import datetime
import pandas as pd
from tqdm import tqdm
import numpy as np


class Portfolio:
    def __init__(self, name_port=None):
        self.name_port = name_port
        self.portfolio = self._select()
        self.env = read_yaml('configs/environment.yaml')

    def _select(self):
        if self.name_port is None:
            portfolio = None
        else:
            portfolio = read_yaml('configs/portfolio.yaml')[self.name_port]

        return portfolio

    def get_portfolio(self):

        res = []
        day = datetime.date.today()

        for ticker in tqdm(self.portfolio):
            t = yf.Ticker(ticker)
            df = pd.DataFrame()
            df['date'] = [day]
            df['ticker'] = [ticker]

            info = t.info
            df['price'] = Ticker(ticker).last_price()
            df['amount'] = [self.portfolio[ticker]]
            df["currency"] = info["currency"]
            df['circulatingSupply'] = info['circulatingSupply']
            df['type'] = info['quoteType']

            if info["dividendYield"]:
                df["yield"] = info["dividendYield"]
            else:
                df["yield"] = None

            try:
                df['sector'] = info['sector']
            except:
                df['sector'] = 'Crypto'

            res.append(df)

        self.df = pd.concat(res)

    def unification(self):

        self.get_portfolio()

        df = self.df
        # Convert to desired currency
        Converter(df)._convert(currency=self.env["CURRENCY"], col_ind='currency', col_currency='price')
        df['value'] = df.price * df.amount

        # Caclulate percentage
        df['percentage'] = df.value / df.value.sum()

        # Formatting
        df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))
        df = df.sort_values('value', ascending=False)

        df["dividends"] = df["yield"] * df.price * df.amount

        # Is always true for now
        if 'passive_income' not in list(df):
            df['passive_income'] = df['dividends']

        self.df = df


if __name__ == "__main__":
    pd.set_option("expand_frame_repr", False)
    d = Portfolio('aram')
    d.unification()
    print(d.df)
    make_percentage(df=d.df, value='value', groupby='sector')