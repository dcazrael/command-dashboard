import pytest
from src.main import CommandDashboard

@pytest.fixture
def app():
    return CommandDashboard()
