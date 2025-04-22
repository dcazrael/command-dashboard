# tests/widgets/test_category_button.py

import pytest
from src.widgets.category_button import CategoryButton
from src.utils.icon_map import ICON_MAP
from textual.app import App
from textual.widgets import Label


class DummyApp(App):
    def compose(self):
        yield CategoryButton("python")


@pytest.mark.asyncio
async def test_category_button_icon_display():
    app = DummyApp()
    async with app.run_test() as pilot:
        button = app.query_one(CategoryButton)
        label_widget = button.query_one(Label)
        expected_icon = ICON_MAP.get("python", "\uf03e")
        assert expected_icon in str(label_widget.renderable)
