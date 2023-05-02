"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize("price,quantity, total", [(10000, 20, 200000)])
def test_price_t(price, quantity, total):
    assert price * quantity == total


@pytest.mark.parametrize("price,pay_rate,total", [(10000, float(0.8), float(8000.0))])
def test_apply_disc(price, pay_rate, total):
    assert price * pay_rate == total


def test_repr():
    item1 = Item('Айфон', 100000, 10)
    assert repr(item1) =="Item('Айфон', 100000, 10)"

def test_str():
    item2 = Item('Радио', 100000, 10)
    assert str(item2) =='Радио'

