from tenbagger.src.interactive.candlestick import candlestick


def test_candlestick():
    ticker = 'ibm'
    candlestick(ticker=ticker, period='1y', interval='1d')