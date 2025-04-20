from textual.widgets import Button
from rich.text import Text
from textual import log
from command_dashboard.utils.utilities import replace_umlauts


class CategoryButton(Button):
    def __init__(self, category: str, icon: str = ""):
        category_id = replace_umlauts(category).replace(" ", "_").replace("/", "_")
        self.category = category
        label = f"{icon} {category.capitalize()}" if icon else category.capitalize()
        super().__init__(label = label, id=f"btn-{category_id}")
