from textual.widget import Widget
from datetime import datetime
from rich.align import Align
from rich.panel import Panel
from rich.columns import Columns
from tenbagger.src.utils.utilities import Ticker


class Indices(Widget):

    def on_mount(self):
        self.set_interval(3, self.refresh)

    def _init_indices(self):
        self.dict_indices = {
            ':netherlands: AEX': '^AEX',
            ':european_union: Europe 50': '^STOXX50E',
            ':united_states: USA 500': '^GSPC',
            ':united_states: USA TECH 100': '^NDX',
            ':germany: Germany 40': '^GDAXI',
            ':united_kingdom: UK 100': '^FTSE'
        }

        self.dict_indices = {k: Ticker(v) for k, v in self.dict_indices.items()}
        self.init_prices = {k: v.last_price() for k, v in self.dict_indices.items()}

        # get prices at close
        self.init_close_prices = {k: v.get_last_day_close() for k, v in self.dict_indices.items()}

    def _percentage_change(self, last_price, symbol):
        close_price = self.init_close_prices[symbol]
        diff_perc = (last_price - close_price) / close_price

        if diff_perc >= 0:
            output = f"[bright_green](+{diff_perc:.2%})"
        else:
            output = f"[bright_red]({diff_perc:.2%})"
        return output

    def render(self):

        if not hasattr(self, 'dict_indices'):
            self._init_indices()

        # Get last prices
        last_prices = {k: v.last_price() for k, v in self.dict_indices.items()}
        data = [Panel(f"[b]{k}[/b]\n[yellow]{v:.2f}[/yellow]\n{self._percentage_change(v, k)} ") for k, v in last_prices.items()]
        return Columns(data)


if __name__ == '__main__':
    from rich.console import Console
    c = Console()
    c.print(":netherlands:")