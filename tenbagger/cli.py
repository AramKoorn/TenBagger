import argparse
from tenbagger.version import __version__
from tenbagger.scripts.candlestick import candlestick


def main():
    parser = argparse.ArgumentParser(description="CLI interface for Stock Data",
                                     epilog="Homepage: https://github.com/rahiel/telegram-send")
    
    parser.add_argument("--candle", action="store_true")
    parser.add_argument("--ticker")
    parser.add_argument("--period")
    parser.add_argument("--interval")
    parser.add_argument("--hoi", action="store_true")
    parser.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))
    args = parser.parse_args()

    
    if (args.candle):
        print(args.ticker)
        candlestick(ticker=args.ticker, period=args.period, interval=args.interval)

    return
