import card
import random


# This class represents a standard Deck of cards. We populate the deck using
# two for loops.
class Deck:
    def __init__(self):
        # Instance variable
        self.cards = []
        # Range over the cards
        for suit in card.SUITS:
            for value in card.VALUES:
                # Create a new card object
                new_card = card.Card(value, suit)
                # Append each card to deck
                self.cards.append(new_card)

    # num_cards returns a count of all the cards in the deck.
    def num_cards(self):
        return len(self.cards)

    # displays a card's value.
    def show(self, card):
        print("{}, {}".format(card.suit, card.value))

    # Shuffle the deck and return a random card.
    def shuffle(self):
        while self.cards:
            random_card = random.choice(self.cards)
            self.cards.remove(random_card)
            return (random_card)

    # Pop from beginning of the list?
    def peek(self):
        if (len(self.cards) != 0):
            return self.cards.pop(0)

    # Pop but don't return anything?
    def draw(self):
        self.cards.pop(0)


myDeck = Deck()
print(myDeck.num_cards())
myDeck.show(myDeck.shuffle())
myDeck.show(myDeck.peek())
