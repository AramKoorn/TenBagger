import json
import os
from pathlib import Path
import logging


def read_json(loc : str):
    '''

    :param loc: path to file
    :return: yaml converted to a dictionary
    '''
    with open(loc) as f:
        data = json.load(f)

    return data


def write_json(data, loc):
    with open(loc, 'w') as json_file:
        json.dump(data, json_file)


def read_from_root(file: str):

    cwd = os.getcwd()
    home_path = str(Path.home()) + '/.tenbagger'
    os.chdir(home_path)

    data = read_json(loc=file)
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