from tenbagger.version import __version__
import os
from pathlib import Path
import logging
import json



def read_json(loc : str):
    '''

    :param loc: path to file
    :return: yaml converted to a dictionary
    '''
    with open(loc) as f:
      data = json.load(f)

    return data


def write_json(data, loc):
    with open('person.txt', 'w') as json_file:
      json.dump(data, json_file)


def read_from_root(file: str):

    cwd = os.getcwd()
    home_path = str(Path.home()) + '/.tenbagger'
    os.chdir(home_path)

    data = read_jsonl(loc=file)
    os.chdir(cwd)
    return data 


def create_hidden_folder(name: str):

    cwd = os.getcwd()
    home_path = Path.home()
    os.chdir(home_path)

    if os.path.exists(f".{name}"):
        logging.info("Folder already exist")
        return

    os.mkdir(f".{name}")
    os.chdir(cwd)



CWD = os.getcwd()
DIRECTORY = os.path.abspath(os.path.dirname(__file__))
os.chdir(DIRECTORY)
FILES = ['staking.json', 'portfolio.json', 'environment.json']

HOME_PATH = Path.home()
TENBAGGER_PATH = f'{HOME_PATH}/.tenbagger'
create_hidden_folder('tenbagger')
os.chdir(TENBAGGER_PATH)

HIDDEN_FILES = os.listdir()  # Get files in .tenbagger
for f in set(FILES) - set(HIDDEN_FILES):
    os.chdir(DIRECTORY)
    to_dump = read_json(f'configs/{f}')
    os.chdir(TENBAGGER_PATH)
    write_json(loc=f, dict=to_dump)

os.chdir(CWD)
