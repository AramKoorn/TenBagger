import pandas as pd
import yaml
from pyfiglet import Figlet
import argparse
from tenbagger.scripts.insiders import format_insiders


if __name__ == "__main__":

    f = Figlet(font='slant')

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
    args = parser.parse_args()

    with open(r'configs/ColorCodes.yaml') as file:
        color_config = yaml.load(file, Loader=yaml.FullLoader)

    ticker = args.Ticker
    print(f.renderText(f'Insider: {ticker}'))
    pd.set_option("expand_frame_repr", False)
    df = format_insiders(ticker)
    print(df)