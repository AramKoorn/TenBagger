import yfinance as yf
import pandas as pd
from forex_python.converter import CurrencyRates
import yaml


class Ticker:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def last_price(self):

        try:
            price = self.ticker.history(period='1d', interval='1m')["Close"].tail(1)[0]
        except:
            price = self.ticker().tail(1)["Close"][0]

        return price

    def history_prices(self, dates):

        # Dictionary returning the dates
        return {date: self.ticker.history(date).Close[0] for i, date in enumerate(dates)}


class Converter:
    def __init__(self, df):
        self.df = df
        assert isinstance(df, pd.DataFrame)

    def _convert(self, currency="EUR", col_ind=None, col_currency=None):

        c = CurrencyRates()
        self.df['factor'] = self.df[col_ind].apply(lambda x: c.get_rate(x, currency))
        self.df[col_currency] = self.df.factor * self.df[col_currency]
        self.df[col_ind] = currency
        del self.df['factor']


def read_yaml(loc):

    with open(f'{loc}') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    ticker = "IBM"
    t = Ticker(ticker)

    #przint(t.info)
    t.history_prices(['7d', '1mo', '2mo', '6mo', '1y'])
    print(t.last_price())