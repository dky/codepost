import card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in card.SUITS:
            for value in card.VALUES:
                card_in_deck = (value, "of", suit)
                self.cards.append(card_in_deck)

    def num_cards(self):
        return len(self.cards)

    def shuffle(self):
        pass

    def peek(self):
        pass

    def draw(self):
        pass


myDeck = Deck()
print(myDeck.num_cards())
