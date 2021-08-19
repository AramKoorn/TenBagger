import argparse
from tenbagger.version import __version__
from tenbagger.src.utils.utilities import order_by_month, make_percentage
from pyfiglet import Figlet
from tenbagger.src.configuration.configuration import Configuration
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="CLI interface for Stock Data",
                                     epilog="Homepage: https://github.com/AramKoorn/TenBagger")

    # Configure
    parser.add_argument("--configure", action="store_true")

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

    # Algorand checkecker
    parser.add_argument("--algo", action="store_true")

    # Calculator
    parser.add_argument('-s', "--scenario", action="store_true")
    parser.add_argument("-dg", "--dividendgrowth", help="rate of dividend growth", type=float)
    parser.add_argument("-n", help="Number of months to simulate", type=int)
    parser.add_argument("-sg", "--stockgrowth", help="rate of stonks growth", type=float)
    parser.add_argument("-m", "--monthly", help="monthly payment", type=int)
    parser.add_argument("-c", "--crypto", action='store_false', help="Include crypto")
    parser.add_argument("-r", "--report", action='store_true', help="Generate report to data folder")

    args = parser.parse_args()

    if args.algo:
        from tenbagger.src.crypto.algorand import Algorand

        algo = Algorand()
        
        # This should be an argument
        address = 'WKMYA6PXWIM6L3TO2T3VPR5AJUGRZXJZDU2A2TPLTT7O44YG2N3M4XUH7Y'
        account = algo.get_account_data(address=address)
        print(account)

    if args.configure:
        c = Configuration()
        c.run_configuration()

    if args.scenario:
        from tenbagger.src.passiveIncome.calculator import PassiveIncomeCalculator

        scenario = PassiveIncomeCalculator(args.portfolio)
        scenario.calulate(n=args.n, growth_stock=args.stockgrowth, growth_dividend=args.dividendgrowth,
                          monthly_payment=args.monthly, generate_report=args.report, only_dividend_stocks=args.crypto)

    if args.dividend:
        from tenbagger.src.dividends.div import DividendsPortfolio
        from tenbagger.src.utils.utilities import read_yaml
        from tenbagger.src.terminal.utils import TermPlots

        portfolio = read_yaml('user_data/portfolio/portfolio.yaml')[args.dividend]
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

        # Read configs
        port = list(read_yaml('user_data/portfolio/portfolio.yaml').keys())
        env = read_yaml('user_data/env/environment.yaml')

        NotifyInsider().notify_portfolio(port)
        NotifyPriceTarget().notify_high()
        NotifyPriceTarget().notify_low()

    if args.portfolio and not args.scenario:

        # Clean this up
        from tenbagger.src.portfolio.core import Portfolio
        from tenbagger.src.terminal.utils import TermPlots
        from tenbagger.src.utils.utilities import read_yaml

        pd.set_option("expand_frame_repr", False)

        f = Figlet(font='slant')
        print(f.renderText('Portfolio'))

        # Read in ENV settings
        env = read_yaml('user_data/env/environment.yaml')

        # Print out portfolio
        port = Portfolio(args.portfolio)
        port.unification()
        print(port.df.drop(columns=['circulatingSupply', 'type']))

        # Print passive income
        print(f'\n Total passive income: {port.df.passive_income.sum()} {env["CURRENCY"]} \n')

        # Print portfolio
        by_secor = make_percentage(port.df.groupby('sector').value.sum().reset_index(), 'value', 'sector')
        TermPlots(by_secor[['sector', 'value']]).plot_bar()

        # Print total value
        print(f'Total value of portfolio: {round(port.df.value.sum(), 2) } {env["CURRENCY"]}')

    if args.tracker:
        from tenbagger.src.dashboard.trackerdash import main
        main()
    
    if (args.candle):
        from tenbagger.src.interactive.candlestick import candlestick
        candlestick(ticker=args.ticker, period=args.period, interval=args.interval)

    return
