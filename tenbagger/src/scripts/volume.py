import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.ticker as mtick
import argparse


def volume(ticker="HITIF"):


    t = yf.Ticker(ticker)
    info = t.info
    hist = t.history(period='10d')
    hist = hist.reset_index()
    hist["Date"] = hist["Date"].apply(lambda x: x.strftime("%m/%d/%Y"))

    fig, ax = plt.subplots()
    sns.barplot(data=hist, x='Date', y='Volume', ax=ax)
    # plt.xticks(rotation=45)
    ax.axhline(info['averageDailyVolume10Day'], color='red')

    fmt = '{x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)

    plt.show()

    pass


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('Trading Volume'))

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
    args = parser.parse_args()
    # with open(r'configs/myportfolio.yaml') as file:
    #     config = yaml.load(file, Loader=yaml.FullLoader)

    

    pd.set_option("expand_frame_repr", False)

    volume(args.Ticker)
