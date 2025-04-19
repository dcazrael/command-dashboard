from command_dashboard.widgets.category_button import CategoryButton


def test_category_button_text_and_id():
    btn = CategoryButton("linux")
    assert btn.label == "Linux"
    assert btn.id == "btn-linux"
    assert btn.category == "linux"


def test_category_button_with_icon():
    btn = CategoryButton("sql", icon="🛢️")
    assert btn.label == "🛢️ Sql"
    assert btn.id == "btn-sql"
    assert btn.category == "sql"
