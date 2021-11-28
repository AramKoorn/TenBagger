from tenbagger.src.portfolio.core import Portfolio
from rich.table import Table
from textual import events
from textual.app import App
from textual.widgets import ScrollView
from tenbagger.src.textui.widgets.portfolio import PortfolioTable, SummaryPortfolio
from textual.widgets import Placeholder
from tenbagger.src.textui.widgets.utils import Clock
from tenbagger.src.textui.widgets.indices import Indices


class AlphaPortfolio(App):

    def __init__(self, portfolio, *args, **kwargs):
        self.portfolio = portfolio
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        await self.view.dock(Clock(),  size=3)
        await self.view.dock(SummaryPortfolio(portfolio=self.portfolio), edge="left", size=20)
        await self.view.dock(PortfolioTable(portfolio=self.portfolio), Indices(), edge="top")

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == '__main__':
    port = Portfolio('my_portfolio')
    port.unification()
    AlphaPortfolio.run(portfolio=port)