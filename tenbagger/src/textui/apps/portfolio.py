from tenbagger.src.portfolio.core import Portfolio
from rich.table import Table
from textual import events
from textual.app import App
from textual.widgets import ScrollView
from tenbagger.src.textui.widgets.portfolio import PortfolioTable, SummaryPortfolio
from textual.widgets import Placeholder
from tenbagger.src.textui.widgets.utils import Clock


class MyApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:

        self.body = body = ScrollView(auto_width=True)

        await self.view.dock(body)

        async def add_content():
            table = Table(title="Demo")

            for i in range(20):
                table.add_column(f"Col {i + 1}", style="bold white")
            for i in range(100):
                table.add_row(*[f"cell {i},{j}" for j in range(20)])

            await body.update(table)

        await self.call_later(add_content)


class OverviewPortfolio(App):

    def __init__(self, portfolio, *args, **kwargs):
        self.portfolio = portfolio
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        await self.view.dock(Clock(),  size=3)
        await self.view.dock(SummaryPortfolio(portfolio=self.portfolio), edge="left", size=20)
        await self.view.dock(PortfolioTable(portfolio=self.portfolio), edge="top")

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == '__main__':
    port = Portfolio('aram')
    port.unification()

    OverviewPortfolio.run(portfolio=port, log="textual.log")
