from tenbagger.scripts.utilities import read_yaml


class Crypto:
    def __init__(self, name_port=None):
        self.name_port = name_port
        self.portfolio = self._select()
        self.env = read_yaml('configs/environment.yaml')