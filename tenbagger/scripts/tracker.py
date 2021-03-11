import pandas as pd
import numpy as np 
import yfinance as yf
import yaml
from tqdm import tqdm


def track(config):

    total = []

    for sector in config:
        s = config[sector]

        res = []
        for ind, ticker in tqdm(s.items()):
            t = yf.Ticker(ticker)

            try:
                try:
                    close = t.history(period='1d', interval='1m')["Close"].tail(1)[0]
                except:
                    close = t.history().tail(1)["Close"][0]

                prev_close = t.history("2d").Close[0] 
                change = round((close - prev_close) / prev_close * 100, 2)
            except:
                change = None
            val = [ind, change]
            res.append(val)

        df = pd.DataFrame(data=res, columns=[sector, sector + "Change"])
        total.append(df)

    return pd.concat(total, axis=1)


# if __name__ == "__main__":
    
#     with open(r'configs/trackers.yaml') as file:
#         config = yaml.load(file, Loader=yaml.FullLoader)

#     df = track(config)
#     print(df)
