from rich.table import Table

from textual import events
from textual.app import App
from textual.widgets import ScrollView
from tenbagger.src.portfolio.core import Portfolio


port = Portfolio('aram')
port.unification()
df = port.df

class FrameToApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:

        self.body = body = ScrollView(auto_width=True)

        await self.view.dock(body)

        async def add_content():
            table = Table(title="Portfolio")

            for col in df.columns:
                table.add_column(col, style="magenta")
            for row in df.values.tolist():
                table.add_row(*[str(j) for j in row])
            await body.update(table)

        await self.call_later(add_content)




FrameToApp.run(title="Simple App", log="textual.log")
