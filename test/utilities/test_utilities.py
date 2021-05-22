from tenbagger.src.utils.utilities import read_yaml, add


def test_add():
    assert add(2, 3) == 5


def test_read_yaml():
    cfg = read_yaml('configs/environment.yaml')
    assert "CURRENCY" in cfg.keys()


if __name__ == '__main__':
    test_read_yaml()