from tenbagger.src.utils.utilities import (
    read_from_root,
    read_yaml,
    Ticker,
    make_percentage,
    create_hidden_folder,
)
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal
import os
from pathlib import Path


def test_create_hidden_folder():
    cwd = os.getcwd()
    create_hidden_folder(name="test_folder")

    assert os.getcwd() == cwd

    os.chdir(str(Path.home()))
    assert os.path.exists(".test_folder")

    os.rmdir(".test_folder")
    assert not os.path.exists(".test_folder")


def test_make_percentage():
    df = pd.DataFrame.from_dict(
        {"sector": ["crypto", "technology"], "value": [150, 200]}
    )

    desired = pd.DataFrame.from_dict(
        {
            "sector": ["technology", "crypto"],
            "value": [200, 150],
            "percentage": ["57.14%", "42.86%"],
        }
    )
    res = make_percentage(df, value="value", groupby="sector")

    assert_frame_equal(
        left=desired.reset_index(drop=True), right=res.reset_index(drop=True)
    )


def test_read_yaml():
    cfg = read_from_root("environment.json")
    assert "CURRENCY" in cfg.keys()


class TestTickerInfo:
    def test_stonk_info(self):
        info = Ticker("IBM").get_info()

        desired = {
            "defaultKeyStatistics",
            "details",
            "summaryProfile",
            "recommendationTrend",
            "financialsTemplate",
            "earnings",
            "price",
            "financialData",
            "quoteType",
            "calendarEvents",
            "summaryDetail",
            "symbol",
            "esgScores",
            "upgradeDowngradeHistory",
            "pageViews",
        }

        assert info.keys() == desired

    def test_info_crypto(self):
        info = Ticker("eth-usd").get_info()
        assert info["quoteType"]["quoteType"] == "CRYPTOCURRENCY"


class TestTickerStonk:
    def setup(self):
        self.ticker = Ticker("ibm")

    def test_last_price(self):
        price = self.ticker.last_price()
        assert isinstance(price, np.float64)

    def test_info(self):
        self.ticker.get_info()

    def test_overview(self):
        overview = self.ticker.overview()
        assert list(overview) == [
            "Ticker",
            "price",
            "MarketCap",
            "Shares Outstanding",
            "Dividend Yield",
            "trailingAnnualDividendYield",
            "Short Percentage of Float",
            "Trailing EPS",
            "52 week low",
            "52 week High",
            "heldPercentInsiders",
            "earningsQuarterlyGrowth",
            "priceToSalesTrailing12Months",
            "fair_value",
        ]

    def test_overview_non_dividend_stonk(self):
        assert Ticker("pypl").overview()


class TestTickerCrypto:
    def setup(self):
        self.ticker = Ticker("eth-usd")

    def test_last_price(self):
        price = self.ticker.last_price()
        assert isinstance(price, np.float64)

    def test_overview(self):
        overview = self.ticker.overview()
        overview = list(overview)
        assert overview == [
            "Ticker",
            "price",
            "MarketCap",
            "52 week low",
            "52 week High",
        ]
