from tenbagger.src.portfolio.core import Portfolio
import os
from tenbagger.src.utils.utilities import order_by_month, make_percentage


def test_portfolio_stocks_only():

    portfolio = {'ibm': 50, 'aapl': 50}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df

    assert df.shape[0] == 2
    assert set(df.ticker.values) == {'ibm', 'aapl'}


def test_mix_crypto_stonks():

    portfolio = {'ibm': 50, 'aapl': 50, 'ETH-USD': 100}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df

    assert df.passive_income.isna().sum() == 0
    assert df.shape[0] == 3


def test_currency_coverter():
    portfolio = {'mrk': 1}
    port = Portfolio(portfolio)
    port.unification()