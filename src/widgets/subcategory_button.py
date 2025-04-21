# widgets/subcategory_button.py

from src.widgets.nav_button import NavButton

class SubcategoryButton(NavButton):
    def __init__(self, subcategory: str, category: str):
        super().__init__(key=subcategory, level="subcategory", category=category)
