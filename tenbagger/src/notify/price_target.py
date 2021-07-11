from tenbagger.src.utils.utilities import read_yaml
from tenbagger.src.utils.utilities import Ticker
import subprocess


class NotifyPriceTarget:
    def __init__(self):
        self.env = read_yaml('user_data/env/environment.yaml')
        self.pt = read_yaml('configs/notifications.yaml')

    def notify_high(self):
        stocks = self.pt['price_target_high']

        for ticker, price_target in stocks.items():

            price = Ticker(ticker).last_price()
            if price >= price_target:
                message = f"ALERT {ticker} exceeded your price target and is now: {price}"
                subprocess.call(['telegram-send', message])

    def notify_low(self):
        stocks = self.pt['price_target_low']

        for ticker, price_target in stocks.items():

            price = Ticker(ticker).last_price()
            if price <= price_target:
                message = f"ALERT {ticker} is below your price target with a price of: {price}"
                subprocess.call(['telegram-send', message])


if __name__ == "__main__":
    n = NotifyPriceTarget()
    n.notify_high()
    n.notify_low()


