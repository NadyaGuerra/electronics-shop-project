import pytest
from src.keyboard import Keyboard


@pytest.fixture

def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.change_lang().language == "RU"
    assert kb.change_lang().language == "EN"
