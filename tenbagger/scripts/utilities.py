import yfinance as yf
import pandas as pd
from forex_python.converter import CurrencyRates
import yaml
import numpy as np
import datetime


def make_percentage(df: pd.DataFrame, value: str, groupby: str):
    df = df.groupby(groupby).value.sum().reset_index().sort_values(value, ascending=False).copy()

    # Caclulate percentage
    df['percentage'] = df.value / df.value.sum()

    # Formatting
    df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))

    return df


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

    def overview(self):

        info = self.ticker.info

        overview = {'price': self.last_price(),
         "MarketCap": info['marketCap'],
         'Shares Outstanding': info['sharesOutstanding'],
         'Dividend Yield': info['dividendYield'],
         'trailingAnnualDividendYield': info['trailingAnnualDividendYield'],
         'Short Percentage of Float': info["shortPercentOfFloat"],
         "Trailing EPS": info['trailingEps'],
         '52 week low': info['fiftyTwoWeekLow'],
         '52 week High': info['fiftyTwoWeekHigh'],
         'heldPercentInsiders': info['heldPercentInsiders'],
         'earningsQuarterlyGrowth': info['earningsQuarterlyGrowth'],
         'priceToSalesTrailing12Months': info['priceToSalesTrailing12Months'],
         "Fair Value": 100 * (info['dividendYield'] * self.last_price()) / info['fiveYearAvgDividendYield']
         }

        overview = pd.DataFrame(list(zip(overview.keys(), overview.values())), columns=['Description', 'Value'])
        overview["Value"] = np.round(overview["Value"], 3)
        overview["Value"] = overview.Value.apply(lambda x: "{:,}".format(x))

        return overview

    # This should be faster
    def get_currency(self):
        return self.ticker.info['currency']


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


def order_by_month(df, col):

    # Create mapping dictionary
    mp = {datetime.date(1900, month, 1).strftime('%B'): i for i, month in enumerate(range(1, 13))}
    df['order'] = df[col].map(mp)
    df = df.sort_values('order')
    del df['order']

    return df


if __name__ == "__main__":
    ticker = "mo"
    t = Ticker(ticker)

    #przint(t.info)
    t.history_prices(['7d', '1mo', '2mo', '6mo', '1y'])
    print(t.last_price())
    t.overview()
