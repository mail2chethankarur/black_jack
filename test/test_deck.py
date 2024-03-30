import pytest
import sys
import os

sys.path.append("../")

from app.utils import *

deck = deck()

test_cards_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 1,
    "Q": 2,
    "K": 3,
}


def test_card_values(deck):
    for card in deck:

        assert test_cards_values[str(card.value)] == int(card.card_value)
