# TenBagger
A Command Line Interface (CLI) to analyse your portfolio, stocks and crypto. This library uses the Yahoo finance API so you need to use the same ticker symbols as on Yahoo Finance.

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
- add unit tests
- Fix dashboard for mondays
- Portfolio should take <1 second
- Portfolio over time
- Key Metrics
- Update portfolio using CLI
- Nice terminal colors for printing
- Import the configs
- portfolio show per sector
- make test to run everything in CLI and just check if it works

## Roadmap
- Think about proper unit tests for Dash
- Create docker image
- CI/CD pipeline
- SQL database to store portfolio over time
- Automatic notification for a specific stock
- Dividend simulator

## TODO
- Fix tracking dashboard for the weekend

## MVP
- Automatic configuration
- CICD pipeline
- Make sure that requirements file is correct
