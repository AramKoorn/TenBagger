from tenbagger.src.passiveIncome.dividends import PassiveDividends


class TestPassiveDividends:
    def setup(self):
        self.calc = PassiveDividends('test_calculator')

    def test_passive_dividend(self):
        df = self.calc.calulate_dividends(n=120, growth_stock=0.03, growth_dividend=0.03, monthly_payment=1000,
                                     generate_report=False, only_dividend_stocks=False)