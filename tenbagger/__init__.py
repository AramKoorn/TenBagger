from tenbagger.version import __version__
from tenbagger.src.utils.builtin_utils import read_from_root, read_json, create_hidden_folder, write_json
import os
from pathlib import Path


CWD = os.getcwd()
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIRECTORY)
FILES = ['staking.json', "portfolio.json", "environment.json"]

HOME_PATH = Path.home()
TENBAGGER_PATH = f'{HOME_PATH}/.tenbagger'
create_hidden_folder('tenbagger')
os.chdir(TENBAGGER_PATH)

HIDDEN_FILES = os.listdir()  # Get files in .tenbagger
for f in set(FILES) - set(HIDDEN_FILES):
    os.chdir(DIRECTORY)
    to_dump = read_json(f'configs/{f}')
    os.chdir(TENBAGGER_PATH)
    write_json(loc=f, data=to_dump)

os.chdir(CWD)
