from src.views import sidebar
from src.widgets.category_button import CategoryButton

# Mock return value for list_categories
def mock_list_categories():
    return ["linux", "sql", "python"]

def test_get_category_buttons(monkeypatch):
    # Replace the real list_categories with the mock
    monkeypatch.setattr(sidebar, "list_categories", mock_list_categories)

    buttons = sidebar.get_category_buttons()

    assert len(buttons) == 3
    assert all(isinstance(btn, CategoryButton) for btn in buttons)
    assert [btn.category for btn in buttons] == ["linux", "sql", "python"]
    assert [btn.key for btn in buttons] == ["LINUX", "SQL", "PYTHON"]
