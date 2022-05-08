from bs4 import BeautifulSoup
from requests import get
import json


class Cosmos:
    def __init__(self):
        pass

    def get_account_data(self, address):

        base_url = 'https://api.cosmoscan.net/account/'
        url = base_url + address
        response = get(url)
        bs = BeautifulSoup(response.text, 'html.parser')

        # data
        data = json.loads(bs.text)

        data["amount"] = float(data["balance"]) + float(data["delegated"])

        return data


if __name__ == "__main__":
    c = Cosmos()
    c.get_account_data(address="cosmos1e3x4n8e82m5ywgszuar4yzx5asyay039g0h5k3")