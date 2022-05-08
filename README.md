![Unit Tests](https://github.com/AramKoorn/TenBagger/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/AramKoorn/TenBagger/branch/main/graph/badge.svg?token=O5F0TEQ0DY)](https://codecov.io/gh/AramKoorn/TenBagger)
[![Documentation Status](https://readthedocs.org/projects/tenbagger/badge/?version=latest)](https://tenbagger.readthedocs.io/en/latest/?badge=latest)

# TenBagger, Find your next TenBagger inside your terminal
Why paying for expensive subscriptions to track your portfolio, dividends and crypto? This library aims to be a complete tool to track and analyse your financial portfolio using the Command Line Interface (CLI). All the features of TenBagger will be displayed as a Textual User Interface (TUI) inside your terminal. 

This library uses the [yfinance](https://github.com/ranaroussi/yfinance) API to fetch the market data. So you need to use the ticker symbols as they are on Yahoo finance. This also means that the stability of TenBagger is bound to the stability of Yahoo finance.

## Compatibility 
Linux/macOS or any other unix based system.

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

Configuration files are stored in the user's root folder.

Configure your portfolio

```sh
vi ~/.tenbagger/portfolio.yaml
```

Configure staking rewards
```sh
vi ~/.tenbagger/staking.yaml
```
Configure preferred currency

```sh
vi ~/.tenbagger/environment.yaml
```

Alternatively, you can change the files in the ~/.tenbagger folder with your preferred text editor.

## Usage
Real-time overview of portfolio. The portfolio automatically gets updated with the real-time stock/crypto prices while the app is running. The app can be closed by hitting q or CTRL+C.

```sh
tenbagger --portfolio WSB
```
![Features](./imgs/static/wsb_portfolio.png)

Overview of Bond markets. Currently supported:
- United states (us)
- Germany (germany)

![Features](./imgs/static/bonds.png)

```sh
tenbagger --bonds us 
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

Show different metrics of the listed ticker. Note that this is supported for both stonks and crypto.
```sh
$ tenbagger --overview aapl
$ tenbagger --overview btc-eur

```
![widgets](./imgs/gifs/overview2.gif)


Candlestick chart
```
tenbagger --candle --ticker ibm  --period 700d --interval 1d
```


Run tracker dashboard
```
tenbagger --tracker
```

## Crypto
For some crypto we directly support the network addresses so that you don't have to update the portfolio json file when you buy or sell some of your crypto. E.g.


```
my_crypto:
  algo-eur: "3C5IFPAZLET3FLGGFK5AXN7NISVD3OCOMEZJESCXUNUHDOIPMVKYB4DILM"
  atom-eur: "cosmos1vjnlkndnekvrnfrp5j3wtsvsezlgwfm9cmrqe9"

```
We will add more blockchains over time. Currentlly supported blockchains are:
- Algorand (algo)
- Cosmos (atom)

## Tasks
- [ ] Create on click button to refresh portfolio on demand
  - [ ] red/green if above or below fair value
- [ ] track portfolio over time using postgres as backend
- [ ] GAK
- [x] Portfolio properties
  - [x] Total dividends
  - [x] Total staking rewards
  - [x] Total passive income
- [ ] Pull upcoming ex dividend dates
