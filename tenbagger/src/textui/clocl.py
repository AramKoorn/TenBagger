from datetime import datetime

from rich.align import Align

from textual.app import App
from textual.widget import Widget
from rich.table import Table
import random


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        table = Table()
        table.add_column("Row ID")
        table.add_column("Description")
        table.add_column("Level")

        table.add_row(f"{random.random():.2f}", f"description {random.random():.2f}", "[red]j")
        return Align.center(table, vertical="middle")


class ClockApp(App):
    async def on_mount(self):
        await self.view.dock(Clock())


ClockApp.run()