# tests/widgets/test_subcategory_button.py

from src.widgets.subcategory_button import SubcategoryButton
from src.widgets.nav_button import NavButton

def test_subcategory_button_initialization():
    button = SubcategoryButton("Dateiverwaltung", "linux")
    assert isinstance(button, NavButton)
    assert button.key == "Dateiverwaltung"
    assert button.level == "subcategory"
    assert button.category == "linux"
    assert button.subcategory == "Dateiverwaltung"
