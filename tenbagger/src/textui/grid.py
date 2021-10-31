from textual.app import App
from textual.widgets import Placeholder
from tenbagger.src.textui.portfolio import PortfolioWidget
from tenbagger.src.portfolio.core import Portfolio
from rich.table import Table
import time
from textual import events
from textual.app import App
from textual.widgets import ScrollView
from rich.live import Live
import random
from tenbagger.src.textui.clocl import PortfolioTable, SummaryPortfolio
from rich.panel import Panel
from textual.widget import Widget
from rich.columns import Columns



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
                table.add_column(f"Col {i + 1}", style="magenta")
            for i in range(100):
                table.add_row(*[f"cell {i},{j}" for j in range(20)])

            await body.update(table)

        await self.call_later(add_content)

# port = Portfolio('my_portfolio')
# port.unification()


class SimpleApp(App):

    def __init__(self, portfolio, *args, **kwargs):
        self.portfolio = portfolio
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        #self.set_interval(1, self.refresh)
        #await self.view.dock(PortfolioWidget(name='hoi', portfolio=port).run(), edge="left")
        await self.view.dock(SummaryPortfolio(portfolio=self.portfolio), edge="left", size=20)

        #await self.view.dock(Clock(), edge="left", size=40)
        #await self.view.dock(ScrollView(auto_width=True), edge="top")

        #self.body = body = ScrollView(auto_width=True)
        await self.view.dock(PortfolioTable(portfolio=self.portfolio), edge="top")
        #
        # async def add_content():
        #     table = Table()
        #     table.add_column("Row ID")
        #     table.add_column("Description")
        #     table.add_column("Level")
        #
        #     table.add_row(f"{random.random()}", f"description {random.random()}", "[red]j")
        #
        #     await body.update(table)

       # await self.call_later(add_content)


class MyApp(App):
    def __init__(self, *args, custom_arg, **kwargs):
        self.custom_arg = custom_arg
        super().__init__(*args, **kwargs)
    async def on_mount(self):
        print(self.custom_arg)
# This is the change, no () after MyApp


# Try to put the big table in the main placeholder window


if __name__ == '__main__':
    port = Portfolio('my_portfolio')
    port.unification()

    # MyApp.run(custom_arg=5)

    SimpleApp.run(portfolio=port, log="textual.log")