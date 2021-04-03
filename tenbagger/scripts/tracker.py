import yfinance as yf
import yaml
from tqdm import tqdm
import pandas as pd


def track(config):

    total = []

    for sector in config:

        # Get sector
        s = config[sector]

        res = []
        for ind, ticker in tqdm(s.items()):
            history = yf.Ticker(ticker).history(period='2d')

            try:
                close = history.Close[-1]
                prev_close = history.Close[0]
                change = round((close - prev_close) / prev_close * 100, 2)
            except:
                change = None

            val = [ind, change]
            res.append(val)

        df = pd.DataFrame(data=res, columns=[sector, sector + "Change"])
        total.append(df)

    return pd.concat(total, axis=1)


# if __name__ == "__main__":
#     pd.set_option("expand_frame_repr", False)
#
#     with open(r'configs/trackers.yaml') as file:
#         config = yaml.load(file, Loader=yaml.FullLoader)
#     track(config)