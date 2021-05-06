import yfinance as yf
import pandas as pd
import yaml

def process_dividends(config):

    df = pd.DataFrame()

    for ticker in config['stocks'].keys():

        data = {}

        t = yf.Ticker(ticker)
        info = t.info

        data['ticker'] = [ticker]
        data['price'] = [t.history(period='1d', interval='1m')["Close"].tail(1)[0]]
        data['currency'] = [info['currency']]
        data['dividendYield'] = [info['dividendYield']]
        data['trailingAnnualDividendYield'] = [info['trailingAnnualDividendYield']]
        data['fiveYearAvgDividendYield'] = [info['fiveYearAvgDividendYield']]
        data['earningsQuarterlyGrowth'] = [info['earningsQuarterlyGrowth']]

        df = df.append(pd.DataFrame.from_dict(data))

    return df


if __name__ == "__main__":

    pd.set_option("expand_frame_repr", False)

    with open(r'configs/dividends.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    df = process_dividends(config)