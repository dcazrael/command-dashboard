from textual.widgets import Button
from command_dashboard.commands import COMMANDS
from command_dashboard.widgets.category_button import CategoryButton

def get_subcategory_buttons(category: str) -> list[CategoryButton]:
    return [CategoryButton(subcategory) for subcategory in COMMANDS[category].keys()]