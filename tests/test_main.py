# tests/test_main.py
import pytest
from src.main import CommandDashboard
from textual.widgets import TextArea
from unittest.mock import patch


@pytest.mark.asyncio
async def test_theme_is_registered():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        assert app.theme == "dracula"


@pytest.mark.asyncio
async def test_focus_navigation():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        nav = app.query_one("#navigation")
        assert nav is not None


@pytest.mark.asyncio
async def test_focus_sub_navigation():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        sub_nav = app.query_one("#sub-navigation")
        assert sub_nav is not None


@pytest.mark.asyncio
async def test_focus_output():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        output = app.query_one("#command-navigation")
        assert output is not None


import pytest
from unittest.mock import patch
from src.main import CommandDashboard
from textual.widgets import TextArea

import pytest
from unittest.mock import patch
from src.main import CommandDashboard
from textual.widgets import TextArea


@pytest.mark.asyncio
async def test_copy_command_sets_clipboard():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        command_text = "echo Hello, World!"

        # Nutze DEINE App-Methode
        app.update_text_area("#output-command", command_text)

        with patch.object(app, "copy_to_clipboard") as mock_copy:
            app.action_copy_command()
            mock_copy.assert_called_once_with(command_text)


@pytest.mark.asyncio
async def test_update_text_area_sets_text():
    app = CommandDashboard()
    async with app.run_test() as pilot:
        text = "echo hello"
        area = app.update_text_area("#output-command", text)

        # Jetzt korrekt: Zugriff auf area.document.text
        assert area.document.text == text
