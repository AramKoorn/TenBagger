import yfinance as yf
import yaml
from tqdm import tqdm
import pandas as pd
import datetime


def track(config):

    total = []
    date = pd.to_datetime(datetime.datetime.now().date())
    weekday = datetime.datetime.today().weekday()

    # If it's weekend set day to Friday
    if (weekday == 6):
        date -= datetime.timedelta(2)
    if (weekday == 5):
        date -= datetime.timedelta(1)

    prev_date = date - datetime.timedelta(1)

    for sector in config:
        s = config[sector]

        res = []
        for ind, ticker in tqdm(s.items()):
            history = yf.Ticker(ticker).history(period='7d')

            try:
                close = history.Close[-1]
                prev_close = history.query('Date == @prev_date').Close[0]
                change = round((close - prev_close) / prev_close * 100, 2)
            except:
                change = None

            val = [ind, change]
            res.append(val)

        df = pd.DataFrame(data=res, columns=[sector, sector + "Change"])
        total.append(df)

    return pd.concat(total, axis=1)
