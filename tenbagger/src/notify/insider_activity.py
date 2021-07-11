from tenbagger.src.scripts.insiders import format_insiders
from tenbagger.src.utils.utilities import read_yaml
import pandas as pd
import subprocess


class NotifyInsider:
    def __init__(self):
        self.env = read_yaml('user_data/env/environment.yaml')
        self.today = pd.Timestamp.today()

    def notify_portfolio(self, symbols):

        """
        Checks if there is insider activity within the last week

        :param portfolio:
        :return:
        """

        week_ago = self.today - pd.to_timedelta(7, unit='d')

        for ticker in symbols:
            try:
                df = format_insiders(ticker)
                df['Filing\xa0Date'] = pd.to_datetime(df['Filing\xa0Date'])
                if df[df['Filing\xa0Date'] >= week_ago].shape[0] > 0:
                    url = f'http://openinsider.com/search?q={ticker}'
                    message = f"In the last week there was insider activity for {ticker}. {url}"
                    subprocess.call(['telegram-send', message])
                else:
                    continue
            except:
                print("No insider information available")


if __name__ == "__main__":
    pd.set_option("expand_frame_repr", False)

    port = read_yaml('user_data/portfolio/portfolio.yaml')['aram']
    n = NotifyInsider()
    n.notify_portfolio(port)