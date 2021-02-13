import argparse
import pandas as pd
import yfinance as yf
import yaml


def get_price(ticker):


    ask = yf.Ticker(ticker).info['ask']
    close = yf.Ticker(ticker).info['previousClose']

    print(f"Ticker: {ticker}")
    print(f"Previous close price: {close}")

    if ask > close:
        color = "green"
    else:
        color = 'red'
    print(f"Asking Price: {color_config['PriceColors'][color]}{yf.Ticker(ticker).info['ask']}")
    #print("TEST")
    print(f"Diff: {color_config['PriceColors'][color]}{(ask - close)/close * 100}%")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
    args = parser.parse_args()

    with open(r'configs/ColorCodes.yaml') as file:
        color_config = yaml.load(file, Loader=yaml.FullLoader)

    get_price(ticker=args.Ticker)
