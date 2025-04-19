from command_dashboard.widgets.category_button import CategoryButton

def test_category_button_properties():
    button = CategoryButton("linux")
    assert button.label == "Linux"
    assert button.id == "btn-linux"
    assert button.category == "linux"
