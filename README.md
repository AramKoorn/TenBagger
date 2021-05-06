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
- add unit tests
- Portfolio should take <1 second
- Portfolio over time
- Key Metrics
- Update portfolio using CLI
- Nice terminal colors for printing
- Import the configs
- make test to run everything in CLI and just check if it works

## Roadmap
- Create docker image
- CI/CD pipeline
- SQL database to store portfolio over time
- Dividend simulator
  - In CLI
  - downloable report 
- Mobile App
- cross platform
- WSB word cloud
- twitter word cloud

## MVP
- Automatic configuration
- configuration file
- CICD pipeline
- Make sure that requirements file is correct
  - Test from docker container
- Config files should be moved to a hidden folder
- Documentation
