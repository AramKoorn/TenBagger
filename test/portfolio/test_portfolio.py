from tenbagger.src.portfolio.core import Portfolio
import numpy as np


def test_portfolio_stocks_only():
    portfolio = {'ibm': 50, 'aapl': 50}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df

    assert df.shape[0] == 2
    assert list(df.ticker.values) == ['ibm', 'aapl']


def test_mix_crypto_stonks():
    portfolio = {'ibm': 50, 'aapl': 50, 'ETH-USD': 100}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df

    assert df.shape[0] == 3