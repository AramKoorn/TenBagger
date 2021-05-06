import argparse
from tenbagger.version import __version__
from tenbagger.src.utils.utilities import order_by_month, make_percentage
from pyfiglet import Figlet
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="CLI interface for Stock Data",
                                     epilog="Homepage: https://github.com/AramKoorn/TenBagger")

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

    # Dividends
    parser.add_argument("--dividend")

    # Notifier
    parser.add_argument("--notify", action="store_true")

    # Overview
    parser.add_argument("--overview")

    args = parser.parse_args()

    if args.dividend:
        from tenbagger.src.dividends.div import DividendsPortfolio
        from tenbagger.src.utils.utilities import read_yaml
        from tenbagger.src.terminal.utils import TermPlots

        portfolio = read_yaml('configs/portfolio.yaml')[args.dividend]
        df = DividendsPortfolio(portfolio).calculate()
        df = order_by_month(df.groupby(['month', 'year']).Dividends.sum().reset_index(), col='month')
        del df['year']
        TermPlots(df).plot_bar()
        print(f"Total dividends: {df.Dividends.sum()}")

    if args.overview:
        from tenbagger.src.utils.utilities import Ticker

        print(Ticker(args.overview).overview())

    if args.notify:
        from tenbagger.src.notify.price_target import NotifyPriceTarget
        from tenbagger.src.notify.insider_activity import NotifyInsider
        from tenbagger.src.utils.utilities import read_yaml

        port = list(read_yaml('configs/portfolio.yaml').keys())
        NotifyInsider().notify_portfolio(port)
        NotifyPriceTarget().notify_high()
        NotifyPriceTarget().notify_low()

    if args.portfolio:

        # Clean this up
        from tenbagger.src.portfolio.crypto import Crypto
        from tenbagger.src.terminal import TermPlots

        pd.set_option("expand_frame_repr", False)

        f = Figlet(font='slant')
        print(f.renderText('Portfolio'))

        # Print out portfolio
        port = Crypto(args.portfolio)
        port.unification()
        port.staking_rewards()
        print(port.df.drop(columns=['circulatingSupply', 'type']))

        # Print portfolio
        by_secor = make_percentage(port.df.groupby('sector').value.sum().reset_index(), 'value', 'sector')
        TermPlots(by_secor[['sector', 'value']]).plot_bar()

        # Print total value
        print(f'Total value of portfolio: {port.df.value.sum()}')

    if args.tracker:
        from tenbagger.src.dashboard.trackerdash import main
        main()
    
    if (args.candle):
        from tenbagger.src.interactive.candlestick import candlestick
        candlestick(ticker=args.ticker, period=args.period, interval=args.interval)

    return
