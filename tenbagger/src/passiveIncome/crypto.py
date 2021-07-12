from tenbagger.src.passiveIncome.calculator import PassiveIncomeCalculator


class StakingRewards(PassiveIncomeCalculator):
    def __init__(self, port):
        super().__init__(port=port)
    pass