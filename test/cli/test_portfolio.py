from tenbagger.src.scripts.portfolio import Portfolio
import pytest


@pytest.mark.skip(reason="Need to kill the server. Otherwise will run forever.")
def test_portfolio():

    args = {'portfolio': 'testing'}

    Portfolio()._print_portfolio()


if __name__ == '__main__':
    test_portfolio()