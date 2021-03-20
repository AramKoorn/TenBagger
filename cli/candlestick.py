import pandas as pd
from pyfiglet import Figlet
import argparse
from tenbagger.scripts.candlestick import candlestick


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('CandleStick'))

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
    parser.add_argument('Period', metavar='period', nargs="?",  help='Time period')
    parser.add_argument('Interval', metavar='interval', nargs="?",  help='Time interval')
    args = parser.parse_args()

    pd.set_option("expand_frame_repr", False)

    candlestick(ticker=args.Ticker, period=args.Period, interval=args.Interval)
