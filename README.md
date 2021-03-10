# TenBagger
A Command Line Interface (CLI) to follow your portfolio. Currently supports stock data and crypto data. This library uses the Yahoo finance API so you need to use the same ticker symbols as on Yahoo Finance.

## Installation
python3 setup.py install
pip3 install .

## Features
- Check price
- check portfolio
- Candlestick charts of historical price data
- Volume daytrading past 10 days (check if this works for crypto)

## Crypto 
We use the coinmarketcap API to pull crypto data. In order to use the 
coinmarketcap API you need create an account and generate an API key.

## Improvements
- add unit tests
- Portfolio should take <1 second
- Portfolio over time
- Key Metrics
- Update portfolio using CLI
- Hide CMA API key 
- Nice terminal colors for printing
- Import the configs
- No need for the cma API anymore


