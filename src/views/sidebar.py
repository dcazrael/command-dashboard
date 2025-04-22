# views/main_panel.py
from src.utils.load_commands import list_categories
from src.widgets.category_button import CategoryButton

def get_category_buttons() -> list[CategoryButton]:
    return [CategoryButton(category=cat) for cat in list_categories()]