# utils/load_commands.py
import sys
import importlib
from pathlib import Path

COMMANDS_PATH = Path(__file__).parent.parent / "commands"

def list_categories() -> list[str]:
    # Ignore internal or draft files starting with _ or __
    return [
        f.stem for f in COMMANDS_PATH.glob("*.py")
        if not f.stem.startswith("_") and f.stem != "__init__"
    ]

def load_commands(category:str) -> dict:
    module_path = f"src.commands.{category}"

    try:
        module = importlib.import_module(module_path)
        return getattr(module, "commands", {})
    except Exception as e:
        print(f"[ERROR] Failed to load commands from '{category}: {e}'")
        return {}

