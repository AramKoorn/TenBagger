from tenbagger.scripts.utilities import Converter
import pandas as pd


def test_converter():

    df = pd.DataFrame([[1, "USD"], [2, 'USD']], columns=['value', 'currency'])
    Converter(df)._convert(currency="EUR", col_ind="currency", col_currency="value")
    assert len(list(df)) == 2


if __name__ == "__main__":
    test_converter()
    pass