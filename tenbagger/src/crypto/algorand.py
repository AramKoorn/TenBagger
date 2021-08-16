from bs4 import BeautifulSoup
from requests import get
import json


class Algorand:
    def __init__(self):
        pass

    def get_account_data(self, address):

        base_url = 'https://algoexplorerapi.io/v1/account/'
        url = base_url + address
        response = get(url)
        bs = BeautifulSoup(response.text, 'html.parser')

        # data
        data = json.loads(bs.text)

        # For some reason the API doesnt round
        fct = 1000000

        kys = ['amount', 'amount-without-pending-rewards', 'pending-rewards', 'reward-base', 'rewards', 'balance']

        for k in kys:
            data[k] = data[k] / fct

        return data
