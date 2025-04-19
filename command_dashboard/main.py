from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Static, Footer, Button


class CommandDashboard(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Button("Linux", id="btn-linux"),
                Button("SQL", id="btn-sql"),
                Button("Datentypen", id="btn-datentypen"),
                id="sidebar",
            ),
            Vertical(Static("Sidebar"), id="main-panel")
        )

        yield Footer()


def main():
    app = CommandDashboard()
    app.run()

if __name__ == "__main__":
    main()