import yfinance as yf
import yaml
import datetime
import pandas as pd
from requests import get
import json
from pathlib import Path
import os
import logging
import re
import json


def read_from_root(file: str):

    cwd = os.getcwd()
    home_path = str(Path.home()) + '/.tenbagger'
    os.chdir(home_path)

    dict = read_yaml(loc=file)
    os.chdir(cwd)
    return dict


def create_hidden_folder(name: str):

    cwd = os.getcwd()
    home_path = Path.home()
    os.chdir(home_path)

    if os.path.exists(f".{name}"):
        logging.info("Folder already exist")
        return

    os.mkdir(f".{name}")
    os.chdir(cwd)


def make_percentage(df: pd.DataFrame, value: str, groupby: str):
    df = df.groupby(groupby)['value'].sum().reset_index().sort_values(value, ascending=False).copy()

    # Caclulate percentage
    df['percentage'] = df['value'] / df['value'].sum()

    # Formatting
    df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))

    return df


class Ticker:
    '''
    Get Ticker information
    '''
    def __init__(self, ticker: str):
        '''

        :param ticker: Ticker symbol. E.g. aapl, ibm, tsla
        '''
        self.ticker_name = ticker
        self.ticker = yf.Ticker(ticker)
        self.info = self.get_info()

    def get_last_day_close(self):
        return self.ticker.history().iloc[-2].Close

    def get_info(self):
        """
        Scrapes General company info from Yahoo finance. Copy pasted this from yfinance but is 3x faster.

        @return:
        """

        base_url = 'https://finance.yahoo.com/quote/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        response = get(base_url + self.ticker_name, headers=headers)
        html = response.text
        json_str = html.split('root.App.main =')[1].split(
            '(this)')[0].split(';\n}')[0].strip()
        data = json.loads(json_str)[
            'context']['dispatcher']['stores']['QuoteSummaryStore']

        # return data
        new_data = json.dumps(data).replace('{}', 'null')
        new_data = re.sub(
            r'\{[\'|\"]raw[\'|\"]:(.*?),(.*?)\}', r'\1', new_data)
        info = json.loads(new_data)
        info['summaryDetail']['dividendYield']

        return info

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

        overview = {
         'Ticker': self.ticker_name,
         'price': self.last_price(),
         "MarketCap": f"{info['marketCap']:3,}",
         '52 week low': f"{info['fiftyTwoWeekLow']:.2f}",
         '52 week High': f"{info['fiftyTwoWeekHigh']:.2f}",
         }

        return overview

    def overview_stonks(self, info):

        overview = {
         'Ticker': self.ticker_name,
         'price': self.last_price(),
         "MarketCap": f"{info['marketCap']:3,}",
         'Shares Outstanding': f"{info['sharesOutstanding']:3,}",
         'Dividend Yield': f"{info['dividendYield']:.2%}" if info['dividendYield'] is not None else info['dividendYield'],
         'trailingAnnualDividendYield': f"{info['trailingAnnualDividendYield']:.2%}",
         'Short Percentage of Float': f'{info["shortPercentOfFloat"]:.2%}',
         "Trailing EPS": f"{info['trailingEps']:.2f}",
         '52 week low': f"{info['fiftyTwoWeekLow']:.2f}",
         '52 week High': f"{info['fiftyTwoWeekHigh']:.2f}",
         'heldPercentInsiders': f"{info['heldPercentInsiders']:.2%}",
         'earningsQuarterlyGrowth': f"{info['earningsQuarterlyGrowth']:.2%}" if info['earningsQuarterlyGrowth'] is not None else info['earningsQuarterlyGrowth'],
         'priceToSalesTrailing12Months': f"{info['priceToSalesTrailing12Months']:.2f}"
         }

        # Determine fair value based on dividend
        try:
            fair_value = f"${100 * (info['dividendYield'] * self.last_price()) / info['fiveYearAvgDividendYield']:.2f}"
        except:
            fair_value = None

        overview['fair_value'] = fair_value

        return overview

    def overview(self):
        '''

        :return: Dictionary of key metrics
        '''

        info = self.info

        if info['quoteType']['quoteType'] == "CRYPTOCURRENCY":
            overview = self.overview_crypto({**info['summaryDetail']})
        else:
            overview = self.overview_stonks({**info['defaultKeyStatistics'], **info['summaryDetail']})

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


def write_yaml(loc: str, dict):
    with open(f'{loc}', 'w') as file:
        yaml.dump(dict, file)


def order_by_month(df, col):

    # Create mapping dictionary
    mp = {datetime.date(1900, month, 1).strftime('%B'): i for i, month in enumerate(range(1, 13))}
    df['order'] = df[col].map(mp)
    df = df.sort_values('order')
    del df['order']

    return df


if __name__ == "__main__":

    import time
    start_time = time.time()
    url = 'https://finance.yahoo.com/quote/MSFT'
    response = get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    html = response.text
    json_str = html.split('root.App.main =')[1].split(
        '(this)')[0].split(';\n}')[0].strip()
    data = json.loads(json_str)[
        'context']['dispatcher']['stores']['QuoteSummaryStore']

    # return data
    new_data = json.dumps(data).replace('{}', 'null')
    import re
    new_data = re.sub(
        r'\{[\'|\"]raw[\'|\"]:(.*?),(.*?)\}', r'\1', new_data)

    hoi = json.loads(new_data)
    hoi['summaryDetail']['dividendYield']
    print(hoi)

    yf.Ticker('msft').info
    print("--- %s seconds ---" % (time.time() - start_time))

