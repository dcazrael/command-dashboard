from unicodedata import category

from textual.widgets import Button
from rich.text import Text

class CategoryButton(Button):
    def __init__(self, category: str, icon: str = ""):
        self.category = category
        label = f"{icon} {category.capitalize()}" if icon else category.capitalize()
        super().__init__(label = label, id=f"btn-{category}")