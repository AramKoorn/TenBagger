"""
Example: Portfolio
======================

This example, shows how you view your portfolio
"""

from tenbagger.src.portfolio.core import Portfolio


def main():

    port = Portfolio(PORTFOLIO)
    port.unification()
    print(port.df)




if __name__ == '__main__':

    PORTFOLIO = {
        'IBM': 10,
        'BTC-USD': 0.5,
        'AAPl': 2,
        'ETH-USD': 2,
        'TSLA': 10
    }

    main()
