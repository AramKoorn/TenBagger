import yaml
import pandas as pd
from pyfiglet import Figlet
from tenbagger.scripts.portfolio import Portfolio
import argparse


if __name__ == "__main__":

    f = Figlet(font='slant')
    print(f.renderText('Portfolio'))

    parser = argparse.ArgumentParser(description='Select portfolio.')
    parser.add_argument('Portfolio', metavar='P', help='Name of Portfolio')
    args = parser.parse_args()

    with open(r'configs/portfolio.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pd.set_option("expand_frame_repr", False)

    port = Portfolio(config[args.Portfolio])
    df = port.unification()
    print(df)
    print(f'Total Value Portfolio: {df.value.sum()}')
    print(f'Yearly Dividends: {df.dividends.sum()}')
