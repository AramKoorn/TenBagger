from tenbagger.src.dividends.div import DividendsPortfolio
from tenbagger.src.utils.utilities import order_by_month
import pytest


@pytest.mark.skip(reason="Need to kill the server. Otherwise will run forever.")
def test_month_order():
    port = {'IBM': 2}
    df = DividendsPortfolio(port).calculate()
    df = order_by_month(df, col='month')

    desired = ['February', 'May', 'August', 'November']
    assert list(df.month) == desired