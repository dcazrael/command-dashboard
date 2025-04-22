# tests/views/test_get_subcategory_buttons.py

import pytest
from src.views.main_panel import get_subcategory_buttons

def test_get_subcategory_buttons(monkeypatch):
    mock_data = {
        "Basics": {
            "Echo": {"command": "echo hello", "explanation": "Say hello"}
        },
        "Advanced": {}
    }

    monkeypatch.setattr("src.views.main_panel.load_commands", lambda x: mock_data)
    buttons = get_subcategory_buttons("linux")
    assert len(buttons) == 2
    assert buttons[0].subcategory == "Basics"
