import pytest
from tenbagger.scripts.tracker import track 
import yaml


def test_tracker():

    with open(r'configs/trackers.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    
    track(config)

    pass

if __name__ == '__main__':
    test_tracker()