Let's do an exercise to get some practice writing some basic classes in Python.

We're going to implement a class that represents a deck of cards. We'll define a Card and then a Deck class.

You will be tested on the initialization of your Deck, its

- shuffle() method
- peek() method
- num_cards() method

Note: Although there is an existing shuffle() method in Python, one of the requirements of this assignment is for you to implement your own shuffle.

card.py should have the following constants:

SUITS = ['DIAMONDS', 'SPADES', 'HEARTS', 'CLUBS']
VALUES = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

## card.py should also have a Card class with the following methods:

- __init__() - Constructor for a card.
- suit() - Returns the suit of the card.
- value() - Returns the value of the card.

## deck.py should have a Deck class with the following methods:

- __init__() - Creates a sorted deck of playing cards. 13 values, 4 suits.
- num_cards() - Returns the number of Cards in the Deck.
- shuffle() - Shuffles the deck of cards. (Note: You may not use the random.shuffle() method. You must implement the shuffle yourself.)
- peek() - Draws and returns the top card in the deck. The card should no longer be in the Deck.
- draw() - Draws a card and removes it from the deck. Does not return the card.
