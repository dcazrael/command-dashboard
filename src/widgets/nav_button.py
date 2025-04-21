from textual.widgets import Button
from src.utils.utilities import replace_umlauts


class NavButton(Button):
    def __init__(self, key: str, *, level: str, category=None, subcategory=None):
        self.key = key
        self.level = level
        self.category = category
        self.subcategory = subcategory

        parts = [level, category, subcategory, key]
        slug = "-".join(filter(None, parts))
        slug = replace_umlauts(slug).replace(" ", "-").replace("/", "-")

        super().__init__(label=key, classes=f"{level}-button button")