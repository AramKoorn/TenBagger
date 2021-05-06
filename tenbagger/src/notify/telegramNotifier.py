import subprocess
# import logging
import telegram_send


class Telegram:
    def send_notification(self, message):
        subprocess.call(['telegram-send', message])


if __name__ == "__main__":

    message = "Stock with Ticker: AAPL went up 10%"
    Telegram().send_notification(message=message)