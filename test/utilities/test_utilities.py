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


if __name__ == '__main__':
    test_read_yaml()
