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

    @property
    def dividends(self):
        return sum(self.df.dividends)

    @property
    def total_staking_rewards(self):
        return sum(self.df.staking_rewards)

    @property
    def passive_income(self):
        return sum(self.df.passive_income)

    def _select(self):
        if isinstance(self.name_port, dict):
            portfolio = self.name_port
        else:
            portfolio = read_yaml('user_data/portfolio/portfolio.yaml')[self.name_port]

        return portfolio

    def get_portfolio(self):

        res = []
        day = datetime.date.today()

        for ticker in tqdm(self.portfolio):
            t = Ticker(ticker)
            df = pd.DataFrame()
            df['date'] = [day]
            df['ticker'] = [ticker]

            info = t.get_info()
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

    def unification(self):

        self.get_portfolio()

        df = self.df
        # Convert to desired currency
        c = CurrencyRates()
        df['price'] = df.apply(lambda x: c.convert(x.currency, self.env["CURRENCY"], x.price), axis=1)
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
