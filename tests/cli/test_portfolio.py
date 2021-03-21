import pytest
import sys
import subprocess


def test_portfolio():
    subprocess.call('python3 cli/portfolio.py portfolio_aram', shell=True)
    

