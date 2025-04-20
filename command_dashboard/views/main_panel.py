from command_dashboard.commands import COMMANDS
from command_dashboard.widgets.command_button import CommandButton
from command_dashboard.widgets.subcategory_button import SubcategoryButton

def get_subcategory_buttons(category: str) -> list[SubcategoryButton]:
    return [SubcategoryButton(subcategory, category) for subcategory in COMMANDS[category].keys()]

def get_command_buttons(category: str, subcategory: str) -> list[CommandButton]:
    return [
        CommandButton(command_name=key, category=category, subcategory=subcategory)
        for key in COMMANDS[category][subcategory].keys()
    ]
