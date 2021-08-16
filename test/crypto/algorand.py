from tenbagger.src.crypto.algorand import Algorand


class TestAlgorand:

    def setup(self):
        self.algo = Algorand()

    def test_address(self):

        # Algorand address
        address = 'WKMYA6PXWIM6L3TO2T3VPR5AJUGRZXJZDU2A2TPLTT7O44YG2N3M4XUH7Y'
        account = self.algo.get_account_data(address=address)

        assert isinstance(account, dict)
        assert account['address'] == address
        assert isinstance(account['balance'], float)
