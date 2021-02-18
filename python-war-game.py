from random import shuffle

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.list = []
        filewrite = open("python-war-game-data.py", "w+")
        filewrite.write(f"list_of_cards = [{suit}, {value}]")

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in self.suits:
            for number in range(1, 14):
                self.cards.append(Card(suit, number))
                # print(self.cards)

    def __str__(self):
        return str(self.cards)

deck = Deck()

print(deck)
