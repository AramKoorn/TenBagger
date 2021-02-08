import yfinance as yf
import yaml
import pandas as pd
import datetime


def print_overview(config):

    port = config['portfolio']['stocks']

    res = []
    day = datetime.date.today()
    print(f"Date: {day}")

    for ticker in port:
        t = yf.Ticker(ticker)
        print(f'Ticker: {ticker} \n Share Ownerschip \n {t.get_major_holders()}')


if __name__ == "__main__":

    with open(r'configs/myportfolio.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pd.set_option("expand_frame_repr", False)
    print(config)

    print(print_overview(config))