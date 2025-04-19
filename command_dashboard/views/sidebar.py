from textual.widgets import Button
from command_dashboard.commands import COMMANDS
from command_dashboard.widgets.category_button import CategoryButton

def get_category_buttons() -> list[CategoryButton]:
    return [CategoryButton(category) for category in COMMANDS.keys()]