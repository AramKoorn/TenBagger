import pytest
from tenbagger.src.scripts.tracker import track
import yaml


@pytest.mark.skip(reason="Need to kill the server. Otherwise will run forever.")
def test_tracker():

    with open(r'configs/trackers.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    
    track(config)

    pass

if __name__ == '__main__':
    test_tracker()
