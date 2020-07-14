SUITS = ['DIAMONDS', 'SPADES', 'HEARTS', 'CLUBS']
VALUES = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
          'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def suit(self):
        return self.suit

    def value(self):
        return self.value
