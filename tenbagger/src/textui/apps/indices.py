from textual.app import App
from tenbagger.src.textui.widgets.indices import Indices
from tenbagger.src.utils.utilities import Ticker


class IndicesApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Indices(), edge="top")

    async def on_load(self, event):
        await self.bind("q", "quit")


if __name__ == "__main__":
    IndicesApp.run()
