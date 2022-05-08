from tenbagger.src.portfolio.core import Portfolio
from tenbagger.src.utils.utilities import Ticker


def test_portfolio_stocks_only():

    portfolio = {"ibm": 50, "aapl": 50}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df

    assert df.shape[0] == 2
    assert set(df.ticker.values) == {"ibm", "aapl"}


def test_mix_crypto_stonks():

    portfolio = {"ibm": 50, "aapl": 50, "ETH-USD": 100}
    port = Portfolio(portfolio)
    port.unification()
    df = port.df
    assert df.passive_income.isna().sum() == 0
    assert df.shape[0] == 3

    assert port.dividends
    assert port.total_staking_rewards
    assert port.passive_income


def test_crypto_address():

    portfolio = {
        "ibm": 50,
        "algo-eur": "WKMYA6PXWIM6L3TO2T3VPR5AJUGRZXJZDU2A2TPLTT7O44YG2N3M4XUH7Y",
        "atom-eur": "cosmos1e3x4n8e82m5ywgszuar4yzx5asyay039g0h5k3",
    }
    port = Portfolio(portfolio)
    port.unification()


def test_currency_coverter():
    portfolio = {"mrk": 1}
    port = Portfolio(portfolio)
    port.unification()


def test_pulse():
    portfolio = {
        "ibm": 50,
        "aapl": 50,
    }
    port = Portfolio(portfolio)
    port.unification()
    df = port.df
    columns = set(df)

    # Update portflio

    for x in range(10):
        import time

        start = time.process_time()
        port.pulse()
        print(time.process_time() - start)
    assert columns == set(port.df)
