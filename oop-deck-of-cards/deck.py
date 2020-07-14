import card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in card.SUITS:
            for value in card.VALUES:
                # Initialize a new card object from Card class
                card_init = card.Card(suit, value)
                # Append each card to deck
                self.cards.append(card_init)

    def num_cards(self):
        return len(self.cards)

    def shuffle(self):
        pass

    def peek(self, deck):
        self.deck = deck
        print(self.deck)

    def draw(self):
        pass


myDeck = Deck()
print(myDeck.num_cards())
print(myDeck.peek(Deck))
