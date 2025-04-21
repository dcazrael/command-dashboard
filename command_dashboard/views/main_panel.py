from command_dashboard.utils.load_commands import load_commands
from command_dashboard.widgets.command_button import CommandButton
from command_dashboard.widgets.subcategory_button import SubcategoryButton


def get_subcategory_buttons(category: str) -> list[SubcategoryButton]:
    commands = load_commands(category)
    return [SubcategoryButton(subcategory, category) for subcategory in commands.keys()]

def get_command_buttons(category: str, subcategory: str) -> list[CommandButton]:
    commands = load_commands(category)
    return [
        CommandButton(command_name=key, category=category, subcategory=subcategory)
        for key in commands[subcategory].keys()
    ]
