from tenbagger.src.crypto.blockchains import AllChains
from tenbagger.src.crypto.algorand import Algorand


def test_algo():
    chain = AllChains('algo')
    chain = chain.select_class()
    assert isinstance(chain, Algorand)
