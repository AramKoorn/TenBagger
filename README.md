![Unit Tests](https://github.com/AramKoorn/TenBagger/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/AramKoorn/TenBagger/branch/main/graph/badge.svg?token=O5F0TEQ0DY)](https://codecov.io/gh/AramKoorn/TenBagger)
[![Documentation Status](https://readthedocs.org/projects/tenbagger/badge/?version=latest)](https://tenbagger.readthedocs.io/en/latest/?badge=latest)

# TenBagger, Find your next TenBagger inside your terminal
Why paying for expensive subscriptions to track your portfolio, dividends, crypto and technical analysis? This library aims to be am complete tool to track and analyse your portfolio and do financial analysis using the Command Line Interface (CLI). 

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
```sh
$ tenbagger --portfolio hypothetical_portfolio 

    ____             __  ____      ___     
   / __ \____  _____/ /_/ __/___  / (_)___ 
  / /_/ / __ \/ ___/ __/ /_/ __ \/ / / __ \
 / ____/ /_/ / /  / /_/ __/ /_/ / / / /_/ /
/_/    \____/_/   \__/_/  \____/_/_/\____/ 
                                           

100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:16<00:00,  2.74s/it]
         date    ticker         price  amount currency   yield             sector         value  staking_rewards     apy percentage  dividends  passive_income
0  2021-08-23   BTC-USD  49286.179688     0.5      USD     NaN             Crypto  24643.089844              NaN     NaN     57.39%   0.000000        0.000000
0  2021-08-23      TSLA    706.299988    10.0      USD     NaN  Consumer Cyclical   7062.999878              NaN     NaN     16.45%   0.000000        0.000000
0  2021-08-23   ETH-USD   3314.813721     2.0      USD     NaN             Crypto   6629.627441       487.277617  0.0735     15.44%   0.000000      487.277617
0  2021-08-23  algo-eur      1.163734  2500.0      EUR     NaN             Crypto   2909.335448       162.049984  0.0557      6.78%   0.000000      162.049984
0  2021-08-23       IBM    139.619995    10.0      USD  0.0472         Technology   1396.199951              NaN     NaN      3.25%  65.900635       65.900635
0  2021-08-23      AAPl    149.710007     2.0      USD  0.0059         Technology    299.420013              NaN     NaN      0.70%   1.766578        1.766578

 Total passive income: 716.9948143439361 USD 


Crypto           : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.18K
Consumer Cyclical: ▇▇▇▇▇▇▇▇▇▇ 7.06 K
Technology       : ▇▇ 1.70 K

Total value of portfolio: 42940.67 USD
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

Get latest ticker information

```sh
$ tenbagger --overview ibm


                     Description              Value
0                          price             139.62
1                      MarketCap  125,144,195,072.0
2             Shares Outstanding      896,320,000.0
3                 Dividend Yield              0.047
4    trailingAnnualDividendYield              0.047
5      Short Percentage of Float              0.029
6                   Trailing EPS              5.917
7                    52 week low             105.92
8                   52 week High             152.84
9            heldPercentInsiders              0.001
10       earningsQuarterlyGrowth             -0.026
11  priceToSalesTrailing12Months              1.682
12                    fair_value             148.76

```


Candlestick chart
```
tenbagger --candle --ticker ibm  --period 700d --interval 1d
```

Get overview of latest ticker information


Run tracker dashboard
```
tenbagger --tracker
```

Candlestick chart 
```
tenbagger --candle --ticker IBM --period 700d --interval 1d
```

## Crypto

Because everything is stored on the the blockchain it's quite easy to directly pull your crypto balance from the blockchain. However, every blockchain got it's own API so we are going to add more crypto over time. The advantage is that you can input your blockchain address in your crypto wallet directly in the portfolio config and all you account balance changes are automatically updated in the analysis. E.g.

```
# This address is from the algorand foundation
my_portfolio:
  algo-eur: 3C5IFPAZLET3FLGGFK5AXN7NISVD3OCOMEZJESCXUNUHDOIPMVKYB4DILM

```
We will add more blockchains over time. Currentlly supported blockchains are:
- Algorand

## Tasks
- [ ] track portfolio over time using postgres as backend
- [ ] GAK
- [x] Portfolio properties
  - [x] Total dividends
  - [x] Total staking rewards
  - [x] Total passive income
- [ ] Pull upcoming ex dividend dates
- [ ] Use textual for interactive dashboard inside terminal!
- [ ] Update portfolio class
  - [x] portfolio.pulse()
  - [ ] Decide on final design of columns
