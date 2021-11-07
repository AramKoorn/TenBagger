from textual.widget import Widget
from datetime import datetime
from rich.align import Align
from rich.panel import Panel
from textual.app import App


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        return Panel(Align.center(time, vertical="middle", style='bold cyan'))


class ClockApp(App):
    async def on_mount(self):
        await self.view.dock(Clock())


if __name__ == "__main__":
    ClockApp.run()
