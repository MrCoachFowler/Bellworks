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
        self.name = name
        self.boardSize = 3
        self.board = []
        self.showBoard = []
        for i in range(self.boardSize):
            self.showBoard.append('| x |')

    def setUpBoards(self, deck):
        self.board = []
        for i in range(self.boardSize):
            self.board.append(deck.cards.pop(0))

        self.showBoard = []
        for i in range(self.boardSize):
            self.showBoard.append('| x |')

    def replaceCard(self, card):
        #see if the card can be replaced, if so, replace and return the replaced card else return false
        if card.value in ['J', 'Q', 'K']:
            return False
        
        cardShowString = '| ' + card.value + ' |'
        if cardShowString in self.showBoard:
            return False
        
        replaceCardIndex = 0
        replaceString = '| A |'
        if card.value.isdigit():
            replaceCardIndex = int(card.value) - 1
            if replaceCardIndex >= self.boardSize:
                return False
            replaceString = '| ' + card.value + ' |'
        
        self.showBoard[replaceCardIndex] = replaceString
        cardFlipped = self.board[replaceCardIndex]
        self.board[replaceCardIndex] = card
        return cardFlipped
    
    def decideDrawOrDiscard(self, discard, deck):
        print('The discard card is ' + discard.value + '. Do you want the discard (1) or draw a new card (2)?')
        result = input()
        if result == "1":
            return discard
        else:
            return deck.cards.pop(0)
        
    def printBoard(self):
        print(", ".join(self.showBoard))

    def wonRound(self):
        if "| x |" in self.showBoard:
            return False
        else:
            return True