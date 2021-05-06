import os
from subprocess import call


class TermPlots:
    def __init__(self, df):
        self.df = df

    def plot_bar(self):

        self.df.to_csv('cache/test.csv', header=False, index=False)
        call('termgraph cache/test.csv', shell=True)

        # Delete from cache
        os.remove('cache/test.csv')