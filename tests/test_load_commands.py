# tests/utils/load_commands.py

import sys
import types
import pytest
from pathlib import Path
from src.utils import load_commands

def test_list_categories_excludes_internal(tmp_path):
    commands_path = tmp_path / "src" / "commands"
    commands_path.mkdir(parents=True)
    (commands_path / "__init__.py").write_text("")
    (commands_path / "linux.py").write_text("commands = {}")
    (commands_path / "_draft.py").write_text("commands = {}")
    (commands_path / "__temp__.py").write_text("commands = {}")

    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(load_commands, "COMMANDS_PATH", commands_path)

    categories = load_commands.list_categories()
    assert "linux" in categories
    assert "_draft" not in categories
    assert "__temp__" not in categories


def test_load_commands_valid_category(tmp_path):
    # build directory
    src_dir = tmp_path / "src"
    commands_path = src_dir / "commands"
    commands_path.mkdir(parents=True)

    # convert src/ and commands/ to package
    (src_dir / "__init__.py").write_text("")
    (commands_path / "__init__.py").write_text("")

    # create testcat module
    testcat_file = commands_path / "testcat.py"
    testcat_file.write_text(
        "commands = {'Test': {'Command': {'command': 'echo', 'explanation': 'test'}}}"
    )

    # make src visible to sys.path
    sys.path.insert(0, str(tmp_path))

    # patch
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(load_commands, "COMMANDS_PATH", commands_path)

    # load module initially
    module_name = "src.commands.testcat"
    import importlib.util
    spec = importlib.util.spec_from_file_location(module_name, testcat_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    # test
    result = load_commands.load_commands("testcat")
    assert "Test" in result

