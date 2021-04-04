from tenbagger.scripts.portfolio import Portfolio
import pytest

def test_proportion_portfolio():
    portfolio = {'IBM': 10, 'ABBV': 2}
    port = Portfolio(portfolio)
    df = port.unification()
    df.percentage.str.replace('%', "").astype('float').sum()
    assert df.percentage.str.replace('%', "").astype('float').sum() == 100

if __name__ == '__main__':
    #test_proportion_portfolio()

    def subsetSum(A, n, sum):

        # return true if the sum becomes 0 (subset found)
        if sum == 0:
            return True

        # base case: no items left, or sum becomes negative
        if n < 0 or sum < 0:
            return False

        # Case 1. Include the current item `A[n]` in the subset and recur
        # for the remaining items `n-1` with the remaining total `sum-A[n]`
        include = subsetSum(A, n - 1, sum - A[n])

        # Case 2. Exclude the current item `A[n]` from the subset and recur for
        # the remaining items `n-1`
        exclude = subsetSum(A, n - 1, sum)

        # return true if we can get subset by including or excluding the
        # current item
        return include or exclude

    set = [7, 3, 2, 5, 8 ]
    target = 14
    subsetSum(set, len(set) - 1, 21)