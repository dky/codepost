import card


class Deck:

    def __init__(self):
        # Instance variable
        self.cards = []
        # Range over the cards
        for suit in card.SUITS:
            for value in card.VALUES:
                new_card = (value, "of", suit)
                # Append each card to deck
                self.cards.append(new_card)

    def num_cards(self):
        return len(self.cards)

    def return_deck(self):
        print(self.cards)

    def shuffle(self):
        pass

    # Pop from beginning of the list?
    def peek(self):
        return self.cards.pop(0)

    # Pop but don't return anything?
    def draw(self):
        self.cards.pop(0)


myDeck = Deck()
print(myDeck.num_cards())
# print(myDeck.return_deck())
# print(myDeck.peek())

print(myDeck.draw())
# This returns 51 elements.
print(myDeck.num_cards())
