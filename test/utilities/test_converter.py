from tenbagger.src.utils.utilities import Converter, Ticker
import pandas as pd
import numpy as np


def test_fair_value_no_div():
    ticker = 'sono'
    overview = Ticker(ticker).overview()
    assert list(overview.loc[overview.Description == 'fair_value', 'Value'])[0] == 'nan'


def test_fair_value_div():
    ticker = 'ibm'
    overview = Ticker(ticker).overview()
    assert list(overview.loc[overview.Description == 'fair_value', 'Value'])[0] != 'nan'


def test_converter():

    df = pd.DataFrame([[1, "USD"], [2, 'USD']], columns=['value', 'currency'])
    Converter(df)._convert(currency="EUR", col_ind="currency", col_currency="value")
    assert len(list(df)) == 2


if __name__ == "__main__":
    test_converter()
    pass