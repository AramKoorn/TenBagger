from tenbagger.src.crypto.algorand import Algorand
from tenbagger.src.crypto.cosmos import Cosmos


class AllChains(Algorand):
    def __init__(self, token_symbol):
        self.token_symbol = token_symbol

    def select_class(self):
        if self.token_symbol.lower() == "algo":
            return Algorand()
        if self.token_symbol.lower() == "atom":
            return Cosmos()
