import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
parser.add_argument('Ticker', metavar='T', help='Ticker Symbol')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

args = parser.parse_args()

url = f'https://www.marketwatch.com/investing/stock/{args.Ticker}/financials/income/quarter'
print(args.Ticker)
df = pd.read_html(url)
print(df)

#print(args.accumulate(args.integers))

# if __name__ == '__main__':
#     main