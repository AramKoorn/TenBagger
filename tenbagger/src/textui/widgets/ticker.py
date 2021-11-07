from tenbagger.src.utils.utilities import Ticker
from textual.widget import Widget
from datetime import datetime
from rich.align import Align
from rich.panel import Panel
from textual.app import App
from rich.columns import Columns


class TickerSummary(Widget):

    def __init__(self, ticker):
        super().__init__(ticker)
        self.ticker = ticker

    def on_mount(self):
        self.set_interval(10, self.refresh)

    def render(self):
        overview = self.ticker.overview()
        return Columns([Panel(f"[b]{k}[/b]\n[yellow]{v}") for k, v in overview.items()])


if __name__ == '__main__':
    TickerSummary(Ticker('aapl'))
