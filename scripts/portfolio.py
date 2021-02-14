import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet
from scripts.crypto import CoinMarketCap


class Portfolio:
    def __init__(self):
        self.crypto = None
        self.stocls = None


    def stocks_portfolio(self):

        port = config['portfolio']['stocks']

        res = []
        day = datetime.date.today()

        for ticker in port:
            t = yf.Ticker(ticker)
            df = pd.DataFrame()
            df['date'] = [day]
            df['ticker'] = [ticker]

            info = t.info

            if info['ask'] is not None:
                df['price'] = [info['ask']]
                df["PoT"] = 'ask'
            else:
                df['price'] = [(info['dayHigh'] + info['dayLow']) / 2]
                df["PoT"] = 'H div L'
            df['amount'] = [port[ticker]]

            res.append(df)

        df = pd.concat(res)
        df['value'] = df.price * df.amount

        # Query from object
        self.stocks = df

        return df

    def crypto_portfolio(self):

        port = config['portfolio']['crypto']

        if len(port.keys()) == 0:
            return pd.DataFrame()

        for symbol, amount in port.items():
            cma = CoinMarketCap()
            info = cma.get_coin_data(symbol=symbol)

            df = pd.DataFrame()
            df['date'] = [datetime.date.today()]
            df['ticker'] = [symbol]
            df['price'] = [info[0]['quote']['USD']['price']]
            df["PoT"] = 'ask'
            df['amount'] = [amount]
            df['value'] = df.price * df.amount

            self.crypto = df

    def unification(self):

        self.stocks_portfolio()
        self.crypto_portfolio()

        df = pd.concat([self.stocks, self.crypto])
        df['percentage'] = df.value / df.value.sum()

        # Formatting
        df['percentage'] = df.percentage.apply(lambda x: "{:.2%}".format(x))
        df = df.sort_values('value', ascending=False)

        return df


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('Portfolio'))

    with open(r'configs/myportfolio.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pd.set_option("expand_frame_repr", False)

    port = Portfolio()
    df = port.unification()
    print(df)
    print(f'Total Value Portfolio: {df.value.sum()}')