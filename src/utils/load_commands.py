import importlib
import os
from pathlib import Path
from src.utils.icon_map import get_icon_for_category

COMMANDS_PATH = Path(__file__).parent.parent / "commands"

def list_categories() -> list[str]:
    # Ignore internal or draft files starting with _ or __
    return [
        f.stem for f in COMMANDS_PATH.glob("*.py")
        if not f.stem.startswith("_") and f.stem != "__init__"
    ]

def load_commands(category:str) -> dict:
    try:
        module = importlib.import_module(f"command_dashboard.commands.{category}")
        return module.commands
    except Exception as e:
        print(f"[ERROR] Failed to load commands from '{category}: {e}")
        return {}
