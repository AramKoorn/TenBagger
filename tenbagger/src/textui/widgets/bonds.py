from textual.widget import Widget
from textual.widget import Panel
from rich.table import Table
from rich import box
from tenbagger.src.treasuries.bonds import Bonds


class BondsPanel(Widget):
    def __init__(self, bonds):
        super().__init__(bonds)
        self.bonds = bonds

    def create_content(self):
        b = Bonds(self.bonds)
        info = b.get_info()
        content = f'[b]10 year {self.bonds}[/b]\n[yellow] {info["current_10_year"]}[/yellow]\n\n'
        return Panel(content)

    def render(self):
        return self.create_content()


class BondsWidget(Widget):
    def __init__(self, market):
        super().__init__(market)
        self.market = market

    def generate_table(self, market):

        b = Bonds(market)
        info = b.get_info()

        df = info["all_bonds"]
        table = Table(title=f"[b][bright_blue]Bonds")

        for col in df.columns:
            table.add_column(col, style="bold white")
        for row in df.values.tolist():
            cur_row = dict(zip(list(df), row))
            table.add_row(*[str(j) for j in list(cur_row.values())])

        # Some formatting
        table.box = box.SIMPLE_HEAD
        table.border_style = "bold blue"

        for col in table.columns:
            col.header_style = "bright_yellow"

        return table

    def render(self):
        table = self.generate_table(market=self.market)
        return table
