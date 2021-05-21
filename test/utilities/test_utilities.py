from tenbagger.src.utils.utilities import read_yaml
import pytest


@pytest.mark.skip(reason="Need to kill the server. Otherwise will run forever.")
def test_read_yaml():
    cfg = read_yaml('configs/environment.yaml')
    assert "CURRENCY" in cfg.keys()


if __name__ == '__main__':
    test_read_yaml()