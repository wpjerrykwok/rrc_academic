# COMP2040 Python Essentials With Data Analysis
# Assignment 6: Deck of Cards
# Wai Ping KWOK
# Create a reusable model of a deck of cards
# using the object-oriented programming paradigm
# Created on 2023 02 03
# Sample output:
# suit:
# 6 of hearts
# 6 of clubs
# That's not a suit!
# J of dinosaurs
# numbers:
# A of spades
# K of spades
# That's not a number in a deck of cards!
# P of diamonds
# [2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts,
# 7 of hearts, 8 of hearts, 9 of hearts, 10 of hearts, J of hearts,
# Q of hearts, K of hearts, A of hearts,
# 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs,
# 7 of clubs, 8 of clubs, 9 of clubs, 10 of clubs, J of clubs,
# Q of clubs, K of clubs, A of clubs,
# 2 of diamonds, 3 of diamonds, 4 of diamonds, 5 of diamonds, 6 of diamonds,
# 7 of diamonds, 8 of diamonds, 9 of diamonds, 10 of diamonds, J of diamonds,
# Q of diamonds, K of diamonds, A of diamonds,
# 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades,
# 7 of spades, 8 of spades, 9 of spades, 10 of spades, J of spades,
# Q of spades, K of spades, A of spades]


class Card:
    """
    for creating playing card objects
    """
    def __init__(self, suit: str, number: str) -> None:
        """
        initialise a card with two attributes\n
        args:
            suit (str): a value from ['hearts', 'clubs', 'diamonds', 'spades']
            number (str): a value from ["2", "3", "4", "5", "6", "7", "8", "9",
                "10", "J", "Q", "K", "A"]\n
        returns:
            empty
        """
        # to indicate these attributes should not be accessed directly
        self._suit = suit
        self._number = number

    def __repr__(self) -> str:
        """
        override the default output to show the card as str\n
        args:
            empty
        returns:
            self.number + ' of ' + self.suit (str): the number and \n
            the suit of a deck of cards
        """
        return self.number + ' of ' + self.suit

    # create a getter
    # a decorator to say that this method is a property
    # add additional behaviour to a class
    @property
    def suit(self) -> str:
        """
        a getter for suit\n
        args:
            empty
        returns:
            self._suit (str): the suit in card
        """
        return self._suit

    # create a setter
    # a decorator to say that it is a setter for suit
    @suit.setter
    def suit(self, suit: str) -> str:
        """
        a setter for suit\n
        args:
            suit(str)
        returns:
            self._suit (str): the suit in card
            or error prompt
        """
        if suit in ['hearts', 'clubs', 'diamonds', 'spades']:
            self._suit = suit
        else:
            print("That's not a suit!")

    # create a getter
    # a decorator to say that this method is a property
    # add additional behaviour to a class
    @property
    def number(self) -> str:
        """
        a getter for number\n
        args:
            empty
        returns:
            self._number (str): the number in card
        """
        return self._number

    # create a setter
    # a decorator to say that it is a setter for number
    @number.setter
    def number(self, number: str) -> str:
        """
        a setter for number\n
        args:
            number(str)
        returns:
            self._number (str): the number in card
            or error prompt
        """
        if number in [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']:
            self._number = number
        else:
            print("That's not a number in a deck of cards!")


class Deck:

    def __init__(self) -> None:
        """
        initialise a deck of card and print it\n
        args:
            empty
        returns:
            empty
        """
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self) -> None:
        """
        populate a deck of card with every suit and every number\n
        args:
            empty
        returns:
            empty
        """
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        numbers = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        # simple Python list comprehensions
        self._cards = [Card(s, n) for s in suits for n in numbers]


# instantiate a Card object
my_card_01 = Card("hearts", "6")
print("suit:")
print(my_card_01)

my_card_01.suit = "clubs"               # change to valid suit
print(my_card_01)

my_card_01.suit = "dinosaurs"           # change to invalid suit

my_card_02 = Card("dinosaurs", "J")     # create with invalid suit
print(my_card_02)

my_card_03 = Card("spades", "A")
print("numbers:")
print(my_card_03)

my_card_03.number = "K"                 # change to valid number
print(my_card_03)

my_card_03.number = "W"                 # change to invalid number

my_card_04 = Card("diamonds", "P")     # create with invalid number
print(my_card_04)

# instantiate a Deck object
my_deck = Deck()
