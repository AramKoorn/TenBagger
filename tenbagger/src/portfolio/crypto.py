from tenbagger.src.utils.utilities import read_yaml
import numpy as np
import pandas as pd


class PortfolioCrypto:
    def __init__(self):
        self.apy = read_yaml('configs/staking.yaml')

    def staking_rewards(self, df : pd.DataFrame):
        df['staking_rewards'] = df.ticker.str.lower().map(self.apy) * df['value']
        df['apy'] = df.ticker.str.lower().map(self.apy)

        return df