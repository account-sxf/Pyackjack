import random


class Card:
    __slots__ = ("suit", "name", "value")

    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return self.__str__()


def get_shuffled_deck():
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    name_val = (
        ("Ace", 11),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("Jack", 10),
        ("Queen", 10),
        ("King", 10),
    )
    deck = [Card(s, n[0], n[1]) for n in name_val for s in suits]
    random.shuffle(deck)
    return deck
