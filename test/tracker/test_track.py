from tenbagger.src.scripts.tracker import track


def test_tracker():
    tickers = {"sector": {"sono": "sono"}}
    df = track(tickers)

    col = ['sector', 'sectorChange']
    assert list(df) == col
    assert df.shape == (1, 2)


# Create test in clo
if __name__ == "__main__":
    test_tracker()