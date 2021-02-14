from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class CoinMarketCap:

    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    def connect(self):

        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '53905295-63b0-4aee-851e-6fabfa8961f0',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(self.url, params=parameters)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return data

    def get_coin_data(self, symbol):

        # Make connection
        data = self.connect()

        # Get Curernt data
        info = [x for x in data['data'] if symbol in x.values()]

        return info