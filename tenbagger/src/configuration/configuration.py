import os
import yfinance as yf
import yaml


class Configuration:

    def _validate_input(self, inp):
        split = inp.split(' ')

        if len(split) != 2:
            print('You should enter <TICKER_SYMBOL #>')
            self.add_entry()

        ticker = split[0]
        amount = float(split[1])

        if yf.Ticker(ticker).history().shape[0] == 0:
            print(
                f'There is no data about ticker {ticker} available on yahoo finance make sure you have the correct ticker')
            self.add_entry()

        return ticker, amount


    def add_entry(self):
        print('You can add an entry by specifying <TICKER_SYMBOL #> E.g. IBM 50 if you own 50 IBM shares')
        inp = input()
        ticker, amount = self._validate_input(inp)
        return ticker, amount


    def create_portfolio(self):

            portfolio = {}

            while True:
                ticker, amount = self.add_entry()
                portfolio[ticker] = amount
                print('Record has successfully been added. \n Do you want to add another record to your portfolio? yes/no')
                inp = input()
                if inp == 'yes':
                    continue
                else:
                    if len(portfolio) > 0:
                        save_loc = 'user_data/portfolio/portfolio.yaml'
                        with open(f'{save_loc}', 'w') as yaml_file:
                            yaml.dump(portfolio, yaml_file, default_flow_style=False)

                        print(
                            f'Successfully recorded your portfolio and is saved to: {save_loc} \n Portfolio: \n {portfolio}')
                    break

    def run_configuration(self):

        print('Do you want to create your portfolio? yes/no')
        inp = input()
        if inp == 'yes':
            self.create_portfolio()
        else:
            print(
                'No portfolio created. Alternatively you can create your portfolio manually by adding/modifying the user_data/portfolio/portfolio.yaml file')


if __name__ == '__main__':
    c = Configuration()
    c.run_configuration()