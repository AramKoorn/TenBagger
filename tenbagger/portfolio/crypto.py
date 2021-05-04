from tenbagger.portfolio.core import Portfolio
import pandas as pd
from tenbagger.scripts.utilities import read_yaml
import numpy as np
from tenbagger.scripts.utilities import make_percentage


class Crypto(Portfolio):
    def __init__(self, name_port):
        super().__init__(name_port)

    def staking_rewards(self):
        rewards = read_yaml('configs/staking.yaml')
        self.df['staking_rewards'] = self.df.ticker.str.lower().map(rewards) * self.df['value']

        if 'passive_income' not in list(self.df):
            self.df['passive_income'] = self.df['staking_rewards']
        else:
            self.df['passive_income'] = np.where(self.df.staking_rewards.notna(), self.df.staking_rewards, self.df.passive_income)


if __name__ == "__main__":
    pd.set_option("expand_frame_repr", False)
    d = Crypto('aram')
    d.unification()
    d.staking_rewards()
    d.df.passive_income.sum()