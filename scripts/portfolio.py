import yfinance as yf
import yaml
import pandas as pd
import datetime
from pyfiglet import Figlet


def portfolio_value(config):

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
    df['percentage'] = df.value / df.value.sum()
    df = df.sort_values('value', ascending=False)

    return df


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('Portfolio'))

    with open(r'configs/myportfolio.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pd.set_option("expand_frame_repr", False)

    df = portfolio_value(config)
    print(df)
    print(f'Total value: {df.value.sum()}')
