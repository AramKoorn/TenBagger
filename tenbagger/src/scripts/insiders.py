import pandas as pd


def format_insiders(ticker):

    url = f'http://openinsider.com/search?q={ticker}'
    df = pd.read_html(url)[11]

    remove_col = ['X', '1d', '1w', '1m', '6m']
    df = df.drop(columns=remove_col)

    return df


if __name__ == "__main__":

    ticker = 'IBM'
    df = format_insiders(ticker)
    print(df)