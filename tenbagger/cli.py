import argparse
from tenbagger.version import __version__
from tenbagger.scripts.candlestick import candlestick
from tenbagger.scripts.utilities import read_yaml
from pyfiglet import Figlet
import pandas as pd
from tenbagger.notify.price_target import NotifyPriceTarget
from tenbagger.notify.insider_activity import NotifyInsider
from tenbagger.scripts.utilities import read_yaml


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

    # Notifier
    parser.add_argument("--notify", action="store_true")

    args = parser.parse_args()

    if args.notify:
        port = list(read_yaml('configs/portfolio.yaml').keys())
        NotifyInsider().notify_portfolio(port)
        NotifyPriceTarget().notify_high()
        NotifyPriceTarget().notify_low()

    if args.portfolio:

        # Clean this up
        from tenbagger.scripts.portfolio import Portfolio

        f = Figlet(font='slant')
        print(f.renderText('Portfolio'))

        # Print out portfolio
        Portfolio(args.portfolio)._print_portfolio()

    if args.tracker:
        from tenbagger.dashboard.trackerdash import main
        main()
    
    if (args.candle):
        print(args.ticker)
        candlestick(ticker=args.ticker, period=args.period, interval=args.interval)

    return
