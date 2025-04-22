# tests/widgets/test_nav_button.py

from src.widgets.nav_button import NavButton
from textual.widgets import Button


def test_nav_button_initialization():
    key = "Datei kopieren"
    level = "command"
    category = "linux"
    subcategory = "Dateiverwaltung"

    button = NavButton(key=key, level=level, category=category, subcategory=subcategory)

    assert isinstance(button, Button)
    assert button.key == key
    assert button.level == level
    assert button.category == category
    assert button.subcategory == subcategory
    assert button.label == key
    assert f"{level}-button" in button.classes
    assert "button" in button.classes
