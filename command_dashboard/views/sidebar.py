from command_dashboard.utils.load_commands import list_categories
from command_dashboard.widgets.category_button import CategoryButton

def get_category_buttons() -> list[CategoryButton]:
    return [CategoryButton(category=cat) for cat in list_categories()]