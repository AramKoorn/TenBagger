from tenbagger.src.crypto.cosmos import Cosmos


def test_cosmos_balance():
    c = Cosmos()
    data = c.get_account_data(address="cosmos1e3x4n8e82m5ywgszuar4yzx5asyay039g0h5k3")
    assert "amount" in data
