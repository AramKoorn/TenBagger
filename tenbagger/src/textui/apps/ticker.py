from tenbagger.src.textui.widgets.ticker import TickerSummary
from textual.app import App
from tenbagger.src.textui.widgets.utils import Clock
from tenbagger.src.utils.utilities import Ticker


class TickerApp(App):

    def __init__(self, ticker, *args, **kwargs):
        self.ticker = ticker
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        await self.view.dock(Clock(),  size=3)
        await self.view.dock((TickerSummary(self.ticker)), edge="top")

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == "__main__":
    TickerApp.run(ticker=Ticker('btc-eur'))
