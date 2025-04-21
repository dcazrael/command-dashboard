# widgets/command_button.py
from src.widgets.nav_button import NavButton

class CommandButton(NavButton):
    def __init__(self, command_name: str, category: str, subcategory: str):
        super().__init__(
            key=command_name,
            level="command",
            category=category,
            subcategory=subcategory
        )
        self.command_name = command_name
