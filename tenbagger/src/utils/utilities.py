import yfinance as yf
import pandas as pd
from currency_converter import CurrencyConverter
import yaml
import numpy as np
import datetime
import pandas as pd


def make_percentage(df: pd.DataFrame, value: str, groupby: str):
    df = df.groupby(groupby).value.sum().reset_index().sort_values(value, ascending=False).copy()

    # Caclulate percentage
    df['percentage'] = df.value / df.value.sum()

    # Formatting
    df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))

    return df


class Ticker:
    '''
    Get Ticker information
    '''
    def __init__(self, ticker : str):
        '''

        :param ticker: Ticker symbol. E.g. aapl, ibm, tsla
        '''
        self.ticker = yf.Ticker(ticker)

    def last_price(self):
        '''

        :return: Get latest tradable ticker price
        '''

        try:
            price = self.ticker.history(period='1d', interval='1m')["Close"].tail(1)[0]
        except:
            price = self.ticker.history().tail(1)["Close"][0]

        return price

    def history_prices(self, dates):

        # Dictionary returning the dates
        return {date: self.ticker.history(date).Close[0] for i, date in enumerate(dates)}

    def overview_crypto(self, info):

        overview = {'price': self.last_price(),
         "MarketCap": info['marketCap'],
         '52 week low': info['fiftyTwoWeekLow'],
         '52 week High': info['fiftyTwoWeekHigh'],
         }

        overview = pd.DataFrame(list(zip(overview.keys(), overview.values())), columns=['Description', 'Value'])
        overview["Value"] = np.round(overview["Value"], 3)
        overview["Value"] = overview.Value.apply(lambda x: "{:,}".format(x))

        return overview

    def overview_stonks(self, info):

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
         'priceToSalesTrailing12Months': info['priceToSalesTrailing12Months']
         }

        # Determine fair value based on dividend
        try:
            fair_value = 100 * (info['dividendYield'] * self.last_price()) / info['fiveYearAvgDividendYield']
        except:
            fair_value = None

        overview['fair_value'] = fair_value

        overview = pd.DataFrame(list(zip(overview.keys(), overview.values())), columns=['Description', 'Value'])
        overview["Value"] = np.round(overview["Value"], 3)
        overview["Value"] = overview.Value.apply(lambda x: "{:,}".format(x))

        return overview

    def overview(self):
        '''

        :return: Dictionary of key metrics
        '''

        info = self.ticker.info

        if info['quoteType'] == "CRYPTOCURRENCY":
            overview = self.overview_crypto(info)
        else:
            overview = self.overview_stonks(info)

        return overview

    # This should be faster
    def get_currency(self):
        """

        :return: Currency that the ticker shows
        """
        return self.ticker.info['currency']


def read_yaml(loc : str):
    '''

    :param loc: path to file
    :return: yaml converted to a dictionary
    '''

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
