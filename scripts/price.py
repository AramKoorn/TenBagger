import argparse
import pandas as pd
import yfinance as yf


parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')

args = parser.parse_args()
print(yf.Ticker(args.Ticker).info['ask'])


#print(args.accumulate(args.integers))

# if __name__ == '__main__':
#     main