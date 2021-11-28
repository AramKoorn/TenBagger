from textual.widget import Widget
from rich.panel import Panel
from textual.app import App
from rich.columns import Columns
from uniplot import plot
from textual.widgets import Placeholder


class TimeSeries(Widget):

    def __init__(self, ticker):
        super().__init__(ticker)
        self.ticker = ticker

    def on_mount(self):
        self.set_interval(10, self.refresh)

    def render(self):

        return plot([1, 2, 3])


class TestApp(App):

    def __init__(self, ticker, *args, **kwargs):
        self.ticker = ticker
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(),  size=3)

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == '__main__':
    TestApp.run(ticker='aapl')

