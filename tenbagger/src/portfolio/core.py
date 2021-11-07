from tenbagger.src.utils.utilities import read_yaml, Ticker, make_percentage
from tenbagger.src.portfolio.crypto import PortfolioCrypto
import datetime
import pandas as pd
from tqdm import tqdm
from forex_python.converter import CurrencyRates
from tenbagger.src.crypto.blockchains import AllChains
from tenbagger.src.crypto.algorand import Algorand


class Portfolio(PortfolioCrypto):
    def __init__(self, name_port):
        super().__init__()
        self.name_port = name_port
        self.portfolio = self._select()
        self.env = read_yaml('user_data/env/environment.yaml')
        self.tickers = {}
        self.c = CurrencyRates()
        self.ticker_info = {}

    @property
    def weighted_staking_rewards(self):
        return self.df[self.df.sector == "Crypto"].staking_rewards.sum() / self.df[
            self.df.sector == "Crypto"].value.sum() * 100 if not None else 0

    @property
    def weighted_dividend_yield(self):
        return self.df[self.df.sector != "Crypto"].dividends.sum() / self.df[
            self.df.sector != "Crypto"].value.sum() * 100 if not None else 0

    @property
    def weighted_yield(self):
        return self.df.passive_income.sum() / self.df.value.sum() * 100 if not None else 0

    @property
    def dividends(self):
        return sum(self.df.dividends) if not None else 0

    @property
    def total_staking_rewards(self):
        return sum(self.df.staking_rewards.fillna(0)) if not None else 0

    @property
    def passive_income(self):
        return sum(self.df.passive_income) if not None else 0

    @property
    def total_value(self):
        return sum(self.df.value.fillna(0)) if not None else 0

    def _select(self):
        if isinstance(self.name_port, dict):
            portfolio = self.name_port
        else:
            portfolio = read_yaml('user_data/portfolio/portfolio.yaml')[self.name_port]

        return portfolio

    def initialize_portfolio(self):

        res = []
        day = datetime.date.today()

        for ticker in tqdm(self.portfolio):
            t = Ticker(ticker)
            self.tickers[ticker] = t
            df = pd.DataFrame()
            df['date'] = [day]
            df['ticker'] = [ticker]

            info = t.get_info()
            self.ticker_info[ticker] = info
            df['price'] = t.last_price()

            #TODO: Make this nicer
            if isinstance(self.portfolio[ticker], str):
                token_symbol = ticker.split('-')[0]
                chain = AllChains(token_symbol).select_class()
                account = chain.get_account_data(self.portfolio[ticker])
                amount = account['amount']
                df['amount'] = amount
            else:
                df['amount'] = [self.portfolio[ticker]]

            df["currency"] = info['summaryDetail']["currency"]
            df['circulatingSupply'] = info['summaryDetail']['circulatingSupply']
            df['type'] = info['quoteType']['quoteType']

            if info['summaryDetail']["dividendYield"]:
                df["yield"] = info['summaryDetail']["dividendYield"]
            else:
                df["yield"] = None

            try:
                df['sector'] = info['summaryProfile']['sector']
            except:
                df['sector'] = 'Crypto'

            res.append(df)

        self.df = pd.concat(res)

    def pulse(self):
        """
        Queries the last prices and updates the portfolio accordingly

        @return: updated portfolio DataFrame
        """


        # Update pricc
        for ticker in self.df.ticker:

                self.tickers[ticker].last_price()

        self.df['value'] = self.df.price * self.df.amount
        self.df['percentage'] = self.df.value / self.df.value.sum()

        # staking rewards
        self.df = self.staking_rewards(self.df)

        # Formatting
        self.df['percentage'] = self.df.percentage.apply(lambda x: "{:.2%}".format(x))

        # Passive income
        self.df['passive_income'] = self.df[['dividends', 'passive_income']].max(axis=1)

    def unification(self):

        self.initialize_portfolio()

        df = self.df
        # Convert to desired currency
        df['price'] = df.apply(lambda x: self.c.convert(x.currency, self.env["CURRENCY"], x.price), axis=1)
        df['currency'] = self.env["CURRENCY"]
        df['value'] = df.price * df.amount

        # Get staking rewards
        df = self.staking_rewards(self.df)

        # Caclulate percentage
        df['percentage'] = df.value / df.value.sum()

        # Formatting
        df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))
        df = df.sort_values('value', ascending=False)

        df["dividends"] = df["yield"] * df.price * df.amount
        df[['dividends', 'passive_income']] = df[['dividends', 'staking_rewards']].fillna(0)

        # Passive income
        df['passive_income'] = df[['dividends', 'passive_income']].max(axis=1)

        self.df = df
