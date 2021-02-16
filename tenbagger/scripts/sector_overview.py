import pandas as pd
from pyfiglet import Figlet
import yaml
import yfinance as yf


def print_overview(config):

    keep = ['EBITDA  EBITDA', 'EPS (Basic)  EPS (Basic)', 'Sales/Revenue  Sales/Revenue']
    res = []

    for ticker in config.keys():

        country = config[ticker]

        if country == 'USA':
            url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials/income/quarter'
        else:
            url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials/income/quarter?countrycode={country}'

        #print(pd.read_html(url))
        df = pd.read_html(url)[4]
        rename = dict(zip(list(df.iloc[:, 1:6]), ['1', '2', '3', "4", "5"]))
        df = df.rename(columns=rename)
        df['ticker'] = ticker
        df = df[df['Item  Item'].isin(keep)]

        # Get market cap
        marketcap = yf.Ticker(ticker).info['marketCap']
        df['MarketCap'] = marketcap
        res.append(df)

    df = pd.concat(res, axis=0)
    df = df.sort_values("MarketCap")
    df['MarketCap'] = df.MarketCap.apply(lambda x: "{:,}".format(x))

    return df


if __name__ == '__main__':

    f = Figlet(font='slant')
    print(f.renderText('Overview'))

    with open(r'configs/sectors.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pd.set_option("expand_frame_repr", False)

    for sector in config.keys():
        print(print_overview(config[sector]))


