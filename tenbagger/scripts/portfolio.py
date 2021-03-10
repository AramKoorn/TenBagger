import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet
from crypto import CoinMarketCap
from tenbagger.scripts.utilities import Ticker


class Portfolio:
    def __init__(self):
        self.crypto = None
        self.stocks = None


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
            df['price'] = Ticker(ticker).last_price() 
            df['amount'] = [port[ticker]]
            df["currency"] = t.info["currency"]
            res.append(df)

        df = pd.concat(res)
        df['value'] = df.price * df.amount

        # Query from object
        self.stocks = df

        return df


    def unification(self):

        self.stocks_portfolio()

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
