from tenbagger.version import __version__
import os
from pathlib import Path
from tenbagger.src.utils.utilities import create_hidden_folder, read_yaml, write_yaml


CWD = os.getcwd()
DIRECTORY = os.path.abspath(os.path.dirname(__file__))
os.chdir(DIRECTORY)
FILES = ['staking.yaml', 'portfolio.yaml', 'environment.yaml']

HOME_PATH = Path.home()
TENBAGGER_PATH = f'{HOME_PATH}/.tenbagger'
create_hidden_folder('tenbagger')
os.chdir(TENBAGGER_PATH)

HIDDEN_FILES = os.listdir()  # Get files in .tenbagger
for f in set(FILES) - set(HIDDEN_FILES):
    os.chdir(CWD)
    to_dump = read_yaml(f'configs/{f}')
    os.chdir(TENBAGGER_PATH)
    write_yaml(loc=f, dict=to_dump)

os.chdir(CWD)
