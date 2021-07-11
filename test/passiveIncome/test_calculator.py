import pandas as pd
from tenbagger.src.passiveIncome.calculator import PassiveIncomeCalculator


class TestCalculator:
    def setup(self):

        pd.set_option('expand_frame_repr', False)
        portfolio = {'aapl': 50, 'eth-usd': 10}
        self.calc = PassiveIncomeCalculator(port=portfolio)

    def test_calculator_only_div(self):
        # df = self.ca
        df = self.calc.calulate(n=120, growth_stock=0.03, growth_dividend=0.03, monthly_payment=1000,
                                          generate_report=False, only_dividend_stocks=True)
        assert set(df.ticker) == set(['aapl'])

    def test_calculator_mixed(self):
        df = self.calc.calulate(n=120, growth_stock=0.03, growth_dividend=0.03, monthly_payment=1000,
                                          generate_report=False, only_dividend_stocks=False)
        assert set(df.ticker) == set(['eth-usd', 'aapl'])

    def test_passive_mixed(self):
        df = self.calc.calulate(n=120, growth_stock=0.03, growth_dividend=0.03, monthly_payment=1000,
                                          generate_report=False, only_dividend_stocks=False)