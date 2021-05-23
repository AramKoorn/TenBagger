from tenbagger.src.utils.utilities import read_yaml, order_by_month, Ticker
import pandas as pd
import numpy as np


def test_read_yaml():
    cfg = read_yaml('configs/environment.yaml')
    assert "CURRENCY" in cfg.keys()


class TestTicker:
    def setup(self):
        self.ticker = Ticker('ibm')

    def test_last_price(self):
        price = self.ticker.last_price()
        assert isinstance(price, np.float64)

    def test_overview(self):
        overview = self.ticker.overview()
        overview = list(overview.Description)
        assert overview == ['price',
                            'MarketCap',
                            'Shares Outstanding',
                            'Dividend Yield',
                            'trailingAnnualDividendYield',
                            'Short Percentage of Float',
                            'Trailing EPS',
                            '52 week low',
                            '52 week High',
                            'heldPercentInsiders',
                            'earningsQuarterlyGrowth',
                            'priceToSalesTrailing12Months',
                            'fair_value']


if __name__ == '__main__':
    test_read_yaml()
