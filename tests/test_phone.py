import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_add(phone):
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone == 25
    assert phone + phone == 10


def test_sim(phone):
    assert phone.number_of_sim == 2


def test_str(phone):
    assert str(phone)== "iPhone 14"

def test_repr(phone):
    assert "Phone('iPhone 14', 120000, 5, 2)"
