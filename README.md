![Unit Tests](https://github.com/AramKoorn/TenBagger/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/AramKoorn/TenBagger/branch/main/graph/badge.svg?token=O5F0TEQ0DY)](https://codecov.io/gh/AramKoorn/TenBagger)
[![Documentation Status](https://readthedocs.org/projects/tenbagger/badge/?version=latest)](https://tenbagger.readthedocs.io/en/latest/?badge=latest)

# TenBagger, Find your next TenBagger inside your terminal
Why paying for expensive subscriptions to track your portfolio, dividends and crypto? This library aims to be a complete tool to track and analyse your financial portfolio using the Command Line Interface (CLI). All the features of TenBagger will be displayed as Textual User Interface (TUI) inside your terminal. 

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
Real time overview of portfolio. All values are getting autimatically updates while the app is running. 
```sh
tenbagger --portfolio my_portfolio
```

![widgets](./imgs/gifs/portfolio.gif)

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
- [ ] Use Panel/column view for company overview
  - [ ] red/green if above or below fair value
- [ ] track portfolio over time using postgres as backend
- [ ] GAK
- [x] Portfolio properties
  - [x] Total dividends
  - [x] Total staking rewards
  - [x] Total passive income
- [ ] Pull upcoming ex dividend dates
- [x] Use textual for interactive dashboard inside terminal!
- [x] Update portfolio class
  - [x] portfolio.pulse()
  - [x] Decide on final design of columns
