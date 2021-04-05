from tenbagger.scripts.portfolio import Portfolio
import subprocess


def test_portfolio():
    Portfolio()._print_portfolio()
    

if __name__ == '__main__':
    test_portfolio()