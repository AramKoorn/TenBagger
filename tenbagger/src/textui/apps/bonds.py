from textual.app import App
from tenbagger.src.textui.widgets.bonds import Bonds
from textual.widgets import Placeholder
from tenbagger.src.textui.widgets.bonds import BondsWidget, BondsPanel
from tenbagger.src.textui.widgets.utils import Clock


class BondsApp(App):
    def __init__(self, market, *args, **kwargs):
        self.market = market
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        await self.view.dock(Clock(), size=3)
        await self.view.dock(BondsPanel(self.market), edge="left", size=20)
        await self.view.dock(BondsWidget(market=self.market), edge="top")

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == "__main__":
    BondsApp.run(market="us")
