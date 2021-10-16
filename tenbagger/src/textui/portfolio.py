import time
from itertools import cycle
from typing import Dict, List, Tuple

from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.syntax import Syntax
from rich.table import Table
from rich import box
from tenbagger.src.portfolio.core import Portfolio
from textual.views import GridView


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


class PortfolioWidget(GridView):
    def __init__(self, name, portfolio):
        super().__init__(name=name)
        self.name = name
        self.portfolio = portfolio

    def generate_table(self):

        # Update table
        prev_prices = dict(zip(list(self.portfolio.df.ticker), list(self.portfolio.df.price)))
        self.portfolio.pulse()
        df = self.portfolio.df

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

    def run(self, table=None):

        if not table:
            table = self.generate_table()

        with Live(table, refresh_per_second=1, transient=True) as live:  # update 4 times a second to feel fluid
            while True:
                live.update(generate_table(portfolio=self.portfolio))


if __name__ == "__main__":  # pragma: no cover

    port = Portfolio('my_portfolio')
    port.unification()

    port.df
    PortfolioWidget(name='hoi', portfolio=port).run()



