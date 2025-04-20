from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Static, Footer, Button, TextArea

from command_dashboard.commands import COMMANDS
from command_dashboard.views.sidebar import get_category_buttons
from command_dashboard.views.main_panel import get_subcategory_buttons, get_command_buttons
from command_dashboard.widgets.category_button import CategoryButton
from command_dashboard.widgets.command_button import CommandButton
from command_dashboard.widgets.subcategory_button import SubcategoryButton
from textual import log


class CommandDashboard(App):
    CSS_PATH = "style.tcss"

    def __init__(self):
        super().__init__()
        self.active_category: str | None = None
        self.active_subcategory: str | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(id="sidebar"),
            Vertical(Static("Main"), id="main-panel")
        )
        yield Horizontal(
            TextArea(id="output-command"),
            TextArea(id="output-explain"),
            id="output-panel"
        )
        yield Footer()

    def on_mount(self) -> None:
        sidebar = self.query_one("#sidebar")
        sidebar.remove_children()
        sidebar.mount(*get_category_buttons())

    def action_display_subcategories(self, category: str) -> None:
        subcategories = get_subcategory_buttons(category)
        main_panel = self.query_one('#main-panel')
        for child in main_panel.children:
            child.remove()
        main_panel.mount(*subcategories)

    def action_display_commands(self, category: str, subcategory: str) -> None:
        self.active_category = category
        self.active_subcategory = subcategory
        buttons = get_command_buttons(category, subcategory)

        main_panel = self.query_one('#main-panel')
        for child in main_panel.children:
            child.remove()
        main_panel.mount(*buttons)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button

        if isinstance(button, CategoryButton):
            self.active_category = button.category
            self.action_display_subcategories(button.category)

        elif isinstance(button, CommandButton):
            # You may later want to add: show command in output panel here
            command_data = COMMANDS[button.category][button.subcategory][button.command_name]
            self.update_text_area('#output-command', command_data["command"])
            self.update_text_area("#output-explain", command_data["explanation"])

        elif isinstance(button, SubcategoryButton):
            self.action_display_commands(button.category, button.key)


    def update_text_area(self, area_id: str, text: str) -> TextArea:
        area = self.query_one(area_id, TextArea)
        area.replace(text, (0, 0), area.document.end)
        return area


def main():
    app = CommandDashboard()
    app.run()

if __name__ == "__main__":
    main()