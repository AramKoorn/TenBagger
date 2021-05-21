![Unit Tests](https://github.com/geohot/tinygrad/workflows/Unit%20Tests/badge.svg)
![Unit Tests](https://github.com/AramKoorn/TenBagger/actions/workflows/test.yml/badge.svg)


# TenBagger
A Command Line Interface (CLI) to analyse your portfolio, stocks and crypto. Find your next TenBagger inside your terminal. This library uses the Yahoo finance API so you need to use the same ticker symbols as on Yahoo Finance.

Inspired by the legend DeepFuckingValue aka Roarking Kitty.
## Usage
Candlestick chart
```
tenbagger --candle --ticker ibm  --period 700d --interval 1d
```
Or you can do the same thing using abbreviations

```
tenbagger --candle --ticker ibm  -p 700d -i 1d
```

Run tracker dashboard
```
tenbagger --tracker
```

Candlestick chart 
```
tenbagger --candle --ticker IBM --period 700d --interval 1d
```

## Installation
python3 setup.py install
pip3 install .

## Features
- Check price
- check portfolio
- Candlestick charts of historical price data
- Volume daytrading past 10 days (check if this works for crypto)

## Improvements
- add unit tests. Increase that coverage 
- Portfolio should take <1 second
- Portfolio over time
- Update portfolio using CLI
- Nice terminal colors for printing
- make test to run everything in CLI and just check if it works

## TODO
- Implement badges
- Implement CI/CD pipeline
- host docs 
- Add coverage report 
- Dividend simulator
  - In CLI
  - downloable report 
- Make simulation reports

