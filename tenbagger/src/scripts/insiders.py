import pandas as pd
import datetime
import yaml

def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))


def format_insiders(ticker):

    url = f'http://openinsider.com/search?q={ticker}'
    df = pd.read_html(url)[11]

    remove_col = ['X', '1d', '1w', '1m', '6m']
    df = df.drop(columns=remove_col)

    return df


if __name__ == "__main__":

    with open(r'configs/ColorCodes.yaml') as file:
        color_config = yaml.load(file, Loader=yaml.FullLoader)

    ticker = 'IBM'
    df = format_insiders(ticker)
