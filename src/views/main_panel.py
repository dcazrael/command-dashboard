# views/main_panel.py
from src.utils.load_commands import load_commands
from src.widgets.command_button import CommandButton
from src.widgets.subcategory_button import SubcategoryButton


def get_subcategory_buttons(category: str) -> list[SubcategoryButton]:
    commands = load_commands(category)
    return [SubcategoryButton(subcategory, category) for subcategory in commands.keys()]

def get_command_buttons(category: str, subcategory: str) -> list[CommandButton]:
    commands = load_commands(category)
    return [
        CommandButton(command_name=key, category=category, subcategory=subcategory)
        for key in commands.get(subcategory, {}).keys()
    ]
