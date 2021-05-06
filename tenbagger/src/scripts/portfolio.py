import yfinance as yf
import pandas as pd
import datetime
from tenbagger.src.utils.utilities import Ticker, read_yaml, Converter
from tqdm import tqdm


class Portfolio:
    def __init__(self, name_port=None):
        self.name_port = name_port
        self.portfolio = self._select()
        self.env = read_yaml('configs/environment.yaml')

    def _select(self):
        if self.name_port is None:
            portfolio = None
        else:
            portfolio = read_yaml('configs/portfolio.yaml')[self.name_port]

        return portfolio

    def get_portfolio(self):

        res = []
        day = datetime.date.today()

        for ticker in tqdm(self.portfolio):
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

        self.df = pd.concat(res)

    def unification(self):

        self.get_portfolio()

        df = self.df
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

    def _print_portfolio(self):
        if self.name_port is None:
            self.name_port = self.env["MAINPORTFOLIO"]
            self.portfolio = self._select()

        # Get portfolio
        self.unification()

        print(self.df)
        print(f'Total Value Portfolio: {round(self.df.value.sum(), 2)} {self.env["CURRENCY"]}')
        print(f'Yearly Dividends: {round(self.df.dividends.sum(), 2)} {self.env["CURRENCY"]}')


if __name__ == "__main__":
    Portfolio()._print_portfolio()

