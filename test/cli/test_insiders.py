import pytest
import subprocess


def test_insiders_company():
   subprocess.call("python3 cli/insiders.py SONO", shell=True)


def test_insiders_overview():
   subprocess.call("python3 cli/purchases.py", shell=True)
