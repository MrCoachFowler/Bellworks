from random import randint

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getAsString(self):
        return self.value + " of " + self.suit

class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "spades", "clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        shuffledCards = []
        while len(self.cards) > 0:
            randCardIndex = randint(0,len(self.cards) - 1)
            shuffledCards.append(self.cards.pop(randCardIndex))
        self.cards = shuffledCards

class Player:
    def __init__(self, name):
        self.name
        self.hand = []
        self.money = 50
        self.bet = 0

    def drawCards(self, deck):
        for i in range(2):
            self.hand.append(deck.cards.pop(0))

    def showHand(self):
        string = "Player " + self.name + "\n"
        string += "Hand: " + self.hand[0].getAsString() + " | " + self.hand[1].getAsString()
        print(string)

    def 