# widgets/category_button.py
from command_dashboard.widgets.nav_button import NavButton

class CategoryButton(NavButton):
    def __init__(self, category: str):
        super().__init__(key=category.upper(), level="category", category=category)
