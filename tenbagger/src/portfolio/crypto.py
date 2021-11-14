from tenbagger.src.utils.utilities import read_yaml, read_from_root
import pandas as pd


class PortfolioCrypto:
    def __init__(self):
        self.apy = read_from_root('staking.json')

    def staking_rewards(self, df: pd.DataFrame):
        df['staking_rewards'] = df.ticker.str.lower().map(self.apy) * df['value']
        df['apy'] = df.ticker.str.lower().map(self.apy)

        return df