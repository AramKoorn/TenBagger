from tenbagger.version import __version__
import os
from pathlib import Path
import logging


def read_from_root(file: str):

    cwd = os.getcwd()
    home_path = str(Path.home()) + '/.tenbagger'
    os.chdir(home_path)

    dict = read_yaml(loc=file)
    os.chdir(cwd)
    return dict


def create_hidden_folder(name: str):

    cwd = os.getcwd()
    home_path = Path.home()
    os.chdir(home_path)

    if os.path.exists(f".{name}"):
        logging.info("Folder already exist")
        return

    os.mkdir(f".{name}")
    os.chdir(cwd)


def write_yaml(loc: str, dict):
    with open(f'{loc}', 'w') as file:
        yaml.dump(dict, file)


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
    os.chdir(DIRECTORY)
    to_dump = read_yaml(f'configs/{f}')
    os.chdir(TENBAGGER_PATH)
    write_yaml(loc=f, dict=to_dump)

os.chdir(CWD)
