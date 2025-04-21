# widgets/category_button.py
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label

from command_dashboard.utils.icon_map import ICON_MAP
from command_dashboard.widgets.nav_button import NavButton

class CategoryButton(NavButton):
    def __init__(self, category: str):
        icon = ICON_MAP.get(category.lower(), "\uf03e")
        self.icon = icon
        super().__init__(key=category.upper(), level="category", category=category)

    def compose(self) -> ComposeResult:
        with Horizontal(classes="category-button"):
            label = " ".join([self.icon, self.key])
            # yield Label(self.icon, classes="icon")
            # yield Label(self.key, classes="label")
            yield Label(label, classes="label")
