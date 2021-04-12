from tenbagger.dividends.div import DividendsPortfolio
from tenbagger.scripts.utilities import order_by_month

def test_month_order():
    port = {'IBM': 2}
    df = DividendsPortfolio(port).calculate()
    df = order_by_month(df, col='month')

    desired = ['February', 'May', 'August', 'November']
    assert list(df.month) == desired