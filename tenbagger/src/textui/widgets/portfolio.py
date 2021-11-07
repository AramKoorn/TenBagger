from textual.widget import Widget
from rich.table import Table
from rich import box
from rich.panel import Panel


class SummaryPortfolio(Widget):

    def __init__(self, portfolio):
        super().__init__(portfolio)
        self.portfolio = portfolio

    def on_mount(self):
        self.set_interval(10, self.refresh)

    def create_content(self):
        self.portfolio.pulse()
        content = f"[b]Portfolio Value[/b]\n[yellow]:euro: {self.portfolio.total_value:.2f}[/yellow]\n\n" \
                  f"[b]Annual Dividends[/b]\n[yellow]:euro: {self.portfolio.dividends:.2f}[/yellow]\n\n" \
                  f"[b]Annual Staking Rewards[/b]\n[yellow]:euro: {self.portfolio.total_staking_rewards:.2f}[/yellow]\n\n" \
                  f"[b]Annual Passive Income[/b]\n[yellow]:euro: {self.portfolio.passive_income:.2f}[/yellow]\n\n" \
                  f"[b]Dividend Yield[/b]\n[yellow]{self.portfolio.weighted_dividend_yield:.2f}%[/yellow]\n\n" \
                  f"[b]Staking Yield[/b]\n[yellow]{self.portfolio.weighted_staking_rewards:.2f}%[/yellow]\n\n" \
                  f"[b]Weighted Yield[/b]\n[yellow]{self.portfolio.weighted_yield:.2f}%[/yellow]\n" \

        return Panel(content)

    def render(self):
        return self.create_content()


class PortfolioTable(Widget):

    def __init__(self, portfolio):
        super().__init__(portfolio)
        self.portfolio = portfolio

    def on_mount(self):
        self.set_interval(10, self.refresh)

    @staticmethod
    def generate_table(portfolio):

        # Update table
        prev_prices = dict(zip(list(portfolio.df.ticker), list(portfolio.df.price)))
        portfolio.pulse()
        df = portfolio.df

        remove_col = ['circulatingSupply', 'date', 'type']
        df = df.drop(columns=remove_col)

        rename_col = {'ticker': 'Ticker',
                      'price': 'Price',
                      'yield': 'Yield',
                      'amount': "Amount",
                      'currency': "Currency",
                      "sector": "Sector",
                      "value": "Value",
                      "staking_rewards": "Staking Rewards",
                      "apy": "APY",
                      "percentage": "Percentage",
                      "dividends": "Dividends",
                      "passive_income": "Passive Income"}
        df = df.rename(columns=rename_col)

        table = Table(title=f"[b][bright_blue]Portfolio")
        fmt_percents = lambda x: f"{x * 100:.2f}%"

        col_fmt = ['Yield', 'APY']
        for x in col_fmt:
            df[x] = df[x].fillna(0)
            df[x] = df[x].apply(fmt_percents)

        fmt_2 = lambda x: f"{x:.2f}"

        for col in ['Value', 'Dividends', "Staking Rewards", "Passive Income"]:
            df[col] = df[col].fillna(0)
            df[col] = df[col].apply(fmt_2)

        for col in df.columns:
            table.add_column(col, style="bold white")
        for row in df.values.tolist():
            cur_row = dict(zip(list(df), row))
            bool = cur_row["Price"] >= prev_prices[cur_row['Ticker']]
            cur_row['Price'] = f'[bright_green]{cur_row["Price"]:.2f}' if bool else f'[bright_red]{cur_row["Price"]:.2f}'
            table.add_row(*[str(j) for j in list(cur_row.values())])

        # Some formatting
        table.box = box.SIMPLE_HEAD
        table.border_style = 'bold blue'

        for col in table.columns:
            col.header_style = 'bright_yellow'

        return table

    def render(self):
        table = self.generate_table(portfolio=self.portfolio)
        return table
