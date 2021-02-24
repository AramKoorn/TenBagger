import pandas as pd
import numpy as np 
import yfinance as yf
import yaml


def track(config):

    total = []

    for sector in config:
        s = config[sector]

        res = []
        for ind, ticker in s.items():
            t = yf.Ticker(ticker)
            info = t.info

            op = info["open"]
            close = info["previousClose"]
            change = (close - op) / op * 100
            val = [ind, change]
            res.append(val)

        df = pd.DataFrame(data=res, columns=[sector, sector + "Change"])
        total.append(df)

    return pd.concat(total, axis=1)


if __name__ == "__main__":
    
    with open(r'configs/trackers.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    df = track(config)
    print(df)
