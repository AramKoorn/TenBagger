# TenBagger
A Command Line Interface (CLI) to follow your portfolio. Currently supports stock data and crypto data. This library uses the Yahoo finance API so you need to use the same ticker symbols as on Yahoo Finance.

## Usage
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
- add unit tests
- Portfolio should take <1 second
- Portfolio over time
- Key Metrics
- Update portfolio using CLI
- Nice terminal colors for printing
- Import the configs
- make test to run everything in CLI and just check if it works

## Roadmap
- Think about proper unit tests for Dash
- Create docker image
- CI/CD pipeline
- SQL database to store portfolio over time
- Automatic notification for a specific stock
  - ?? Cloud
  - ?? Raspberry PI
- Dividend simulator
