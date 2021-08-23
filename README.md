![Unit Tests](https://github.com/AramKoorn/TenBagger/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/AramKoorn/TenBagger/branch/main/graph/badge.svg?token=O5F0TEQ0DY)](https://codecov.io/gh/AramKoorn/TenBagger)
[![Documentation Status](https://readthedocs.org/projects/tenbagger/badge/?version=latest)](https://tenbagger.readthedocs.io/en/latest/?badge=latest)

# TenBagger
A Command Line Interface (CLI) to analyse your portfolio, stocks and crypto. Find your next TenBagger inside your terminal. This library uses the Yahoo finance API so you need to use the same ticker symbols as on Yahoo Finance.

Inspired by the legend DeepFuckingValue aka Roarking Kitty.

## Installation
```
git clone https://github.com/AramKoorn/TenBagger 
cd TenBagger
python3 setup.py install && pip3 install .
```
Check if installation worked:
```
tenbagger -v
```
## Getting Started

Add/modify a portfolio with

```
tenbagger --configure
```
Alternatively, modify the portfolio.yaml in the user_data/portfolio/ folder.

## Usage
Portfolio overview
```
tenbagger --portfolio my_portfolio
```
```sh
$ tenbagger --portfolio hypothetical_portfolio 

    ____             __  ____      ___     
   / __ \____  _____/ /_/ __/___  / (_)___ 
  / /_/ / __ \/ ___/ __/ /_/ __ \/ / / __ \
 / ____/ /_/ / /  / /_/ __/ /_/ / / / /_/ /
/_/    \____/_/   \__/_/  \____/_/_/\____/ 
                                           

100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:16<00:00,  2.77s/it]
         date    ticker         price  amount currency   yield             sector         value  staking_rewards     apy percentage  dividends  passive_income
0  2021-08-23   BTC-USD  40471.465042     0.5      USD     NaN             Crypto  20235.732521              NaN     NaN     57.40%   0.000000        0.000000
0  2021-08-23      TSLA    581.651971    10.0      USD     NaN  Consumer Cyclical   5816.519705              NaN     NaN     16.50%   0.000000        0.000000
0  2021-08-23   ETH-USD   2717.068017     2.0      USD     NaN             Crypto   5434.136035       399.408999  0.0735     15.42%   0.000000      399.408999
0  2021-08-23  algo-eur      0.947387  2500.0      EUR     NaN             Crypto   2368.468493       131.923695  0.0557      6.72%   0.000000      131.923695
0  2021-08-23       IBM    114.988063    10.0      USD  0.0472         Technology   1149.880630              NaN     NaN      3.26%  54.274363       54.274363
0  2021-08-23      AAPl    123.289143     2.0      USD  0.0059         Technology    246.578287              NaN     NaN      0.70%   1.454812        1.454812

 Total passive income: 587.061868880697 EUR 


Crypto           : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 28.04K
Consumer Cyclical: ▇▇▇▇▇▇▇▇▇▇ 5.82 K
Technology       : ▇▇ 1.40 K

Total value of portfolio: 35251.32 EUR

```

Simulate passive income of dividend payouts and staking rewards

```
# portfolio: Name of portfolio specified in config/portfolio.yaml
# n: number of months
# stockgrowth: yearly Stock growth rate 
# dividendgrowth: yearly dividend growth
# m: montlhy payment
# crypto: boolean to include crypto in simulation
# report: Boolean to generate csv report of simulation

tenbagger --scenario -n 120 --stockgrowth 0.03 --dividendgrowth 0.03 -m 1000 --crypto --report --portfolio my_portfolio

```

Candlestick chart
```
tenbagger --candle --ticker ibm  --period 700d --interval 1d
```

Get overview of latest ticker information

```
tenbagger --overview IBM 
```

Run tracker dashboard
```
tenbagger --tracker
```

Candlestick chart 
```
tenbagger --candle --ticker IBM --period 700d --interval 1d
```

## Features
- Check price
- check portfolio
- Candlestick charts of historical price data
- Volume daytrading past 10 days 

## Improvements
- add unit tests. Increase that coverage 
- Portfolio should take <1 second
- Portfolio over time
- Update portfolio using CLI
- Nice terminal colors for printing
- make test to run everything in CLI and just check if it works

## TODO
- host docs 
