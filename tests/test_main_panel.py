import pytest
from src.views.main_panel import get_subcategory_buttons, get_command_buttons

# Mock data for testing
mock_commands = {
    'category1': {
        'subcategory1': {
            'command1': {'command': 'echo "Hello"', 'explanation': 'Prints Hello'},
            'command2': {'command': 'echo "World"', 'explanation': 'Prints World'},
        },
        'subcategory2': {
            'command3': {'command': 'ls', 'explanation': 'Lists files'},
        },
    },
    'category2': {
        'subcategory3': {
            'command4': {'command': 'pwd', 'explanation': 'Prints working directory'},
        },
    },
}

# Mock load_commands function
def mock_load_commands(category: str):
    return mock_commands.get(category, {})

# Patch the load_commands function in main_panel
@pytest.fixture(autouse=True)
def patch_load_commands(monkeypatch):
    monkeypatch.setattr('src.views.main_panel.load_commands', mock_load_commands)

def test_get_subcategory_buttons_existing_category():
    buttons = get_subcategory_buttons('category1')
    subcategories = [button.subcategory for button in buttons]
    assert set(subcategories) == {'subcategory1', 'subcategory2'}

def test_get_subcategory_buttons_non_existing_category():
    buttons = get_subcategory_buttons('non_existing_category')
    assert buttons == []

def test_get_command_buttons_existing_subcategory():
    buttons = get_command_buttons('category1', 'subcategory1')
    command_names = [button.command_name for button in buttons]
    assert set(command_names) == {'command1', 'command2'}

def test_get_command_buttons_non_existing_subcategory():
    buttons = get_command_buttons('category1', 'non_existing_subcategory')
    assert buttons == []

def test_get_command_buttons_non_existing_category():
    buttons = get_command_buttons('non_existing_category', 'subcategory1')
    assert buttons == []
