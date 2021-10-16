from rich.table import Table

from textual import events
from textual.app import App
from textual.widgets import ScrollView
from tenbagger.src.portfolio.core import Portfolio
from rich.text import Text
import random
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

port = Portfolio('aram')
port.unification()
df = port.df


console = Console()

syntax = Syntax(
    '''def loop_last(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:
"""Iterate and generate a tuple with a flag for last value."""
iter_values = iter(values)
try:
    previous_value = next(iter_values)
except StopIteration:
    return
for value in iter_values:
    yield False, previous_value
    previous_value = value
yield True, previous_value''',
    "python",
    line_numbers=True,
)

table = Table("foo", "bar", "baz")
table.add_row("1", "2", "3")

progress_renderables = [
    "You can make the terminal shorter and taller to see the live table hide"
    "Text may be printed while the progress bars are rendering.",
    Panel("In fact, [i]any[/i] renderable will work"),
    "Such as [magenta]tables[/]...",
    table,
    "Pretty printed structures...",
    {"type": "example", "text": "Pretty printed"},
    "Syntax...",
    syntax,
    Rule("Give it a try!"),
]

examples = cycle(progress_renderables)

exchanges = [
    "SGD",
    "MYR",
    "EUR",
    "USD",
    "AUD",
    "JPY",
    "CNH",
    "HKD",
    "CAD",
    "INR",
    "DKK",
    "GBP",
    "RUB",
    "NZD",
    "MXN",
    "IDR",
    "TWD",
    "THB",
    "VND",
]

def run_live():

    with Live(console=console) as live_table:
        exchange_rate_dict: Dict[Tuple[str, str], float] = {}

        for index in range(100):
            select_exchange = exchanges[index % len(exchanges)]

            for exchange in exchanges:
                if exchange == select_exchange:
                    continue
                time.sleep(0.4)
                if random.randint(0, 10) < 1:
                    console.log(next(examples))
                exchange_rate_dict[(select_exchange, exchange)] = 200 / (
                        (random.random() * 320) + 1
                )
                if len(exchange_rate_dict) > len(exchanges) - 1:
                    exchange_rate_dict.pop(list(exchange_rate_dict.keys())[0])
                table = Table(title="Exchange Rates")

                table.add_column("Source Currency")
                table.add_column("Destination Currency")
                table.add_column("Exchange Rate")

                for ((source, dest), exchange_rate) in exchange_rate_dict.items():
                    table.add_row(
                        source,
                        dest,
                        Text(
                            f"{exchange_rate:.4f}",
                            style="red" if exchange_rate < 1.0 else "green",
                        ),
                    )

                live_table.update(Align.center(table))


class FrameToApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:

        self.body = body = ScrollView(auto_width=True)

        await self.view.dock(body)

        # Can I add a live table to the contect?
        async def add_content():
            run_live()
            # table = Table(title="Portfolio")
            #
            # for col in df.columns:
            #     table.add_column(col, style="magenta")
            # for row in df.values.tolist():
            #     table.add_row(*[str(j) for j in row])
            # await body.update(table)

        await self.call_later(add_content)



if __name__ == '__main__':
    FrameToApp.run(title="Simple App", log="textual.log")
