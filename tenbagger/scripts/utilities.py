import yfinance as yf


class Ticker:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        #self.info = self.ticker.info

    def last_price(self):

        try:
            price = self.ticker.history(period='1d', interval='1m')["Close"].tail(1)[0]
        except:
            price = self.ticker().tail(1)["Close"][0]

        return price


if __name__ == "__main__":
    ticker = "IBM"
    t = Ticker(ticker)
    #print(t.info)
    print(t.last_price())

     
