import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.ticker as mtick
import plotly.graph_objects as go
import argparse


def candlestick(ticker="HITIF", period="365d"):


    t = yf.Ticker(ticker)
    # x`info = t.info
    hist = t.history(period=period)
    hist = hist.reset_index()
    hist["Date"] = hist["Date"].apply(lambda x: x.strftime("%m/%d/%Y"))

    hist
    fig = go.Figure(data=[go.Candlestick(x=hist['Date'],
                                         open=hist.Open,
                                         high=hist.High,
                                         low=hist.Low,
                                         close=hist.Close)])

    fig.show()


    pass


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('CandleStick'))

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
    parser.add_argument('Period', metavar='period', nargs="?",  help='Time interval')
    args = parser.parse_args()

    pd.set_option("expand_frame_repr", False)

    candlestick(ticker=args.Ticker, period=args.Period)