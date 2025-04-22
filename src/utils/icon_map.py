# utils/icon_map.py
ICON_MAP = {
    "bash": "\ue795",
    "powershell": "\ue86c",
    "markdown": "\uf853",
    "linux": "\ue712",
    "python": "\ue73c",
    "java": "\ue738",
    "json": "\ue60b",
    "ini": "\uf07c",
    "django": "\ue71d",
    "vscode": "\ue70c",
    "chatgpt": "\uf0e0",
    "git": "\ue702",
    "numpy": "\ue84a",
    "pandas": "\ue85d",
    "mysql": "\ue704",
    "datentypen": "\uf03e",  # default
}

DEFAULT_ICON = "\uf03e"

def get_icon_for_category(category: str) -> str:
    return ICON_MAP.get(category.lower(), DEFAULT_ICON)