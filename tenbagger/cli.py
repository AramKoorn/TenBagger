import argparse
from tenbagger.version import __version__
from tenbagger.scripts.candlestick import candlestick
from pyfiglet import Figlet
import yaml
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="CLI interface for Stock Data",
                                     epilog="Homepage: https://github.com/rahiel/telegram-send")

    # Portfolio
    parser.add_argument("--portfolio")
    parser.add_argument("--ticker")

    # For Candlestick
    parser.add_argument("--candle", action="store_true")
    parser.add_argument("-p", "--period", help="Period of ticker")
    parser.add_argument("-i", "--interval", help="Interval of stock")

    parser.add_argument("--tracker", action="store_true")
    parser.add_argument("--hoi", action="store_true")
    parser.add_argument('-v', "--version", action="version", version="%(prog)s {}".format(__version__))
    args = parser.parse_args()

    if args.portfolio:

        # Clean this up
        from tenbagger.scripts.portfolio import Portfolio

        f = Figlet(font='slant')
        print(f.renderText('Portfolio'))

        with open(r'configs/portfolio.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        pd.set_option("expand_frame_repr", False)

        port = Portfolio(config[args.portfolio])
        df = port.unification()
        print(df)
        print(f'Total Value Portfolio: {df.value.sum()}')
        print(f'Yearly Dividends: {df.dividends.sum()}')


    if args.tracker:
        from tenbagger.dashboard.trackerdash import main
        main()
    
    if (args.candle):
        print(args.ticker)
        candlestick(ticker=args.ticker, period=args.period, interval=args.interval)

    return
