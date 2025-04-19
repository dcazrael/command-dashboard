from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Static, Footer, Button
from command_dashboard.views.sidebar import get_category_buttons


class CommandDashboard(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(*get_category_buttons(), id="sidebar"),
            Vertical(Static("Sidebar"), id="main-panel")
        )
        yield Footer()


def main():
    app = CommandDashboard()
    app.run()

if __name__ == "__main__":
    main()