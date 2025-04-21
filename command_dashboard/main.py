from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid, Container, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Static, Footer, Button, TextArea

from command_dashboard.utils.load_commands import load_commands
from command_dashboard.themes.theme import darkwave_theme
from command_dashboard.views.sidebar import get_category_buttons
from command_dashboard.views.main_panel import get_subcategory_buttons, get_command_buttons
from command_dashboard.widgets.category_button import CategoryButton
from command_dashboard.widgets.command_button import CommandButton
from command_dashboard.widgets.subcategory_button import SubcategoryButton
from textual import log


class CommandDashboard(App):
    CSS_PATH = "style.tcss"

    BINDINGS = [
        ("n", "focus_navigation", "Focus Navigation"),
        ("s", "focus_sub_navigation", "Focus Subcategories"),
        ("c", "focus_output", "Focus Commands"),
        ("y", "copy_command", "Copy command")
    ]

    def __init__(self):
        super().__init__()
        self.active_category: str | None = None
        self.active_subcategory: str | None = None

    def compose(self) -> ComposeResult:
        yield Header()

        with (Container(id="app-grid")):
            yield VerticalScroll(id="navigation")
            with Container(id="main-panel"):
                yield HorizontalScroll(id="sub-navigation")
                with Container(id="command-panel"):
                    yield VerticalScroll(id="command-navigation")
                    with Container(id="output-panel"):
                        yield Vertical(
                    TextArea(id="output-command"),
                            id="command-wrapper",
                            classes="output-container"
                        )
                        yield Vertical(
                            TextArea(id="output-explain"),
                            id="explanation-wrapper",
                            classes="output-container"
                        )

        yield Footer()

    def on_mount(self) -> None:
        self.register_theme(darkwave_theme)
        self.theme = "darkwave"

        navigation = self.query_one("#navigation")
        navigation.border_title = "navigation".upper()
        navigation.border_subtitle = "n"
        output_command = self.query_one("#command-wrapper")
        output_command.border_title = "command".upper()
        output_command.border_subtitle = "y"
        output_explain = self.query_one("#explanation-wrapper")
        output_explain.border_title = "explanation".upper()
        navigation.remove_children()
        navigation.mount(*get_category_buttons())

    def action_focus_navigation(self) -> None:
        nav = self.query_one("#navigation")
        nav.focus()

    def action_focus_sub_navigation(self) -> None:
        sub_navigation = self.query_one("#sub-navigation")
        sub_navigation.focus()

    def action_focus_output(self) -> None:
        output = self.query_one("#command-navigation")  # or #output_panel
        output.focus()

    def action_copy_command(self) -> None:
        area = self.query_one("#output-command", TextArea)
        text_to_copy = area.text
        self.copy_to_clipboard(text_to_copy)
        self.notify("Copied command to clipboard")

    def action_display_subcategories(self, category: str) -> None:
        subcategories = get_subcategory_buttons(category)
        sub_nav_panel = self.query_one('#sub-navigation')
        sub_nav_panel.border_title = category.upper()
        sub_nav_panel.border_subtitle = "scroll with shift+mousewheel / s"
        for child in sub_nav_panel.children:
            child.remove()
        sub_nav_panel.mount(*subcategories)

    def action_display_commands(self, category: str, subcategory: str) -> None:
        self.active_category = category
        self.active_subcategory = subcategory
        buttons = get_command_buttons(category, subcategory)

        command_nav_panel = self.query_one('#command-navigation')
        command_nav_panel.border_title = subcategory.upper()
        command_nav_panel.border_subtitle = "c"
        for child in command_nav_panel.children:
            child.remove()
        command_nav_panel.mount(*buttons)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button

        if isinstance(button, CategoryButton):
            self.active_category = button.category
            self.action_display_subcategories(button.category)

        elif isinstance(button, CommandButton):
            command_data = load_commands(button.category).get(button.subcategory, {}).get(button.command_name)
            if command_data:
                self.update_text_area('#output-command', command_data["command"])
                self.update_text_area('#output-explain', command_data["explanation"])

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