# tests/widgets/test_command_button.py

from src.widgets.command_button import CommandButton
from src.widgets.nav_button import NavButton

def test_command_button_initialization():
    button = CommandButton("Datei kopieren", "linux", "Dateiverwaltung")
    assert isinstance(button, NavButton)
    assert button.command_name == "Datei kopieren"
    assert button.key == "Datei kopieren"
    assert button.level == "command"
    assert button.category == "linux"
    assert button.subcategory == "Dateiverwaltung"
