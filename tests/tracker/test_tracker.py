from tenbagger.scripts.tracker import track

def test_tracker():
    tickers = {"sector": {"sono": "sono"}}
    df = track(tickers)
    x = 2


if __name__ == "__main__":
    test_tracker()