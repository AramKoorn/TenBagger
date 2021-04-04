import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet
from tenbagger.scripts.utilities import Ticker, read_yaml, Converter
from forex_python.converter import CurrencyRates


class Portfolio:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        assert isinstance(self.portfolio, dict)
        self.env = read_yaml('configs/environment.yaml')
        self.df = None

    def _check_valid(self):

        for value in self.portfolio.values():
            assert isinstance(value, (float, int))

        pass

    def get_portfolio(self):

        res = []
        day = datetime.date.today()

        for ticker in self.portfolio:
            t = yf.Ticker(ticker)
            df = pd.DataFrame()
            df['date'] = [day]
            df['ticker'] = [ticker]

            info = t.info
            df['price'] = Ticker(ticker).last_price() 
            df['amount'] = [self.portfolio[ticker]]
            df["currency"] = info["currency"]

            if info["dividendYield"]:
                df["yield"] = info["dividendYield"]
            else:
                df["yield"] = None

            res.append(df)

        df = pd.concat(res)

        # Query from object
        self.stocks = df

        return df

    def unification(self):

        self.get_portfolio()
        self._check_valid()

        df = pd.concat([self.stocks, None])

        # Convert to desired currency
        Converter(df)._convert(currency=self.env["CURRENCY"], col_ind='currency', col_currency='price')
        df['value'] = df.price * df.amount

        # Caclulate percentage
        df['percentage'] = df.value / df.value.sum()

        # Formatting
        df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))
        df = df.sort_values('value', ascending=False)

        df["dividends"] = df["yield"] * df.price * df.amount
        self.df = df

        return df

    def _print_portfolio(self):
        if self.df is None:
            port = read_yaml('configs/portfolio.yaml')[f'{self.env["MAINPORTFOLIO"]}']
            df = Portfolio(port).unification()

        print(df)
        print(f'Total Value Portfolio: {round(df.value.sum(), 2)} {self.env["CURRENCY"]}')
        print(f'Yearly Dividends: {df.dividends.sum()} {self.env["CURRENCY"]}')


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('Portfolio'))

    with open(r'configs/portfolio.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    port = config['aram']
    pd.set_option("expand_frame_repr", False)

    Portfolio(port)._print_portfolio()

