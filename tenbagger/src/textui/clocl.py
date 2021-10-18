from datetime import datetime

from rich.align import Align

from textual.app import App
from textual.widget import Widget
from rich.table import Table
import random
from rich import box
from tenbagger.src.portfolio.core import Portfolio


port = Portfolio('my_portfolio')
port.unification()


def generate_table(portfolio):

    # Update table
    prev_prices = dict(zip(list(portfolio.df.ticker), list(portfolio.df.price)))
    portfolio.pulse()
    df = portfolio.df

    table = Table(title="Portfolio")

    for col in df.columns:
        table.add_column(col, style="magenta")
    for row in df.values.tolist():
        cur_row = dict(zip(list(df), row))
        bool = cur_row["price"] >= prev_prices[cur_row['ticker']]
        cur_row['price'] = f'[bright_green]{cur_row["price"]:.2f}' if bool else f'[bright_red]{cur_row["price"]:.2f}'
        table.add_row(*[str(j) for j in list(cur_row.values())])

    # Some formatting
    table.box = box.SIMPLE_HEAD

    for col in table.columns:
        col.header_style = 'bright_yellow'

    return table


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        # time = datetime.now().strftime("%c")
        # table = Table()
        # table.add_column("Row ID")
        # table.add_column("Description")
        # table.add_column("Level")
        #
        # table.add_row(f"{random.random():.2f}", f"description {random.random():.2f}", "[red]j")
        table = generate_table(port)
        return table


class ClockApp(App):
    async def on_mount(self):
        await self.view.dock(Clock())


#ClockApp.run()