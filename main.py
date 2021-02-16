import argparse


def main():

    parser = argparse.ArgumentParser(description='Query Information of a Ticker.')
    parser.add_argument('script', metavar='S', help='Name of script')
    parser.add_argument('Ticker', metavar='T', nargs="?",  help='Ticker Symbol')
    parser.add_argument('Period', metavar='period', nargs="?",  help='Time interval')
    args = parser.parse_args()

    
    if args.script == "candlestick":
        
        from tenbagger.scripts.candlestick import candlestick
        candlestick(args.Ticker, args.Period)


    return


if __name__ == "__main__":
    main()

