from textual.widgets import Button

class CategoryButton(Button):
    def __init__(self, category: str):
        super().__init__(
            label=category.capitalize(),
            id=f"btn-{category}"
        )
        self.category = category