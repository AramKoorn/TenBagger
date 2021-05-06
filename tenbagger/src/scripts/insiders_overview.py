import pandas as pd
from tenbagger.src.utils.utilities import Ticker


def clean_insider(df, col):

    df[col] = df[col].str.replace('+', '')
    df[col] = df[col].str.replace(',', '')
    df[col] = df[col].str.replace('$', '')

    df[col] = df[col].astype('float')

    return df


def overview():

    pd.set_option("expand_frame_repr", False)

    df = pd.read_html('http://openinsider.com/')[10]
    clean_cols = ['Qty', 'Price', 'Value']

    for col in clean_cols:
        df = clean_insider(df, col)

    rm_col = ['1d', '1w', '1m', '6m']
    df = df.drop(columns=rm_col)

    dates = ['7d', '1mo', '2mo', '6mo', '1y']
    data = {ticker: Ticker(ticker).history_prices(dates) for i, ticker in enumerate(set(df.Ticker))}

    for t, dat in data.items():
        last_price = Ticker(t).last_price()
        for dt, price in dat.items():
            df.loc[df.Ticker == t, dt] = round((last_price - price) / price * 100, 2)

    # Make it percentage
    for date in dates:
        df[date] = df[date].astype('str') + "%"

    df = df.sort_values('Value', ascending=False)

    return df


if __name__ == '__main__':
    df = overview()
    x = 2