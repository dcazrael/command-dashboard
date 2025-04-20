from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Static, Footer, Button
from command_dashboard.views.sidebar import get_category_buttons
from command_dashboard.views.main_panel import get_subcategory_buttons
from command_dashboard.widgets.category_button import CategoryButton


class CommandDashboard(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(*get_category_buttons(), id="sidebar"),
            Vertical(Static("Sidebar"), id="main-panel")
        )
        yield Footer()

    def action_display_subcategories(self, category: str) -> None:
        subcategories = get_subcategory_buttons(category)
        main_panel = self.query_one('#main-panel')
        main_panel.mount(*subcategories)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button
        if isinstance(button, CategoryButton):
            category = button.category
            self.action_display_subcategories(category)


def main():
    app = CommandDashboard()
    app.run()

if __name__ == "__main__":
    main()