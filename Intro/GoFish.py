from random import randint

class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for suit in suits:
            for i in range(len(names)):
                self.cards.append(Card(suit, names[i], values[i]))

    def shuffle(self):
        shuffledCards = []
        while len(self.cards) > 0:
            randCardIndex = randint(0,len(self.cards)-1)
            shuffledCards.append(self.cards.pop(randCardIndex))
        self.cards = shuffledCards

    def getTopCard(self):
        return self.cards.pop(0)
    
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.sets = []

        
    def askForCard(self):
        print(self.name, ' it is your turn. You have:')
        print(', '.join([card.name for card in self.cards]))
        while True:
            print('What card do you want to ask for?')
            requestedCard = input()
            if requestedCard in [card.name for card in self.cards]:
                return requestedCard
            else:
                print("You don't have that card...")

    def askPlayerForCard(self, requestedCardName, players):
        print('Who do you want to ask?')
        for player in players:
            if player == self:
                continue
            else:
                print(player.name, 'with', str(len(player.cards)), 'cards and', str(len(player.sets)), 'sets')
        while True:
            pName = input()
            if pName in [player.name for player in players]:
                for player in players:
                    if pName == player.name:
                        if player == self:
                            print("You can't choose yourself... Choose another player")
                            continue
                        if requestedCardName in [card.name for card in player.cards]:
                            i = 0
                            while i < len(player.cards):
                                if player.cards[i].name == requestedCardName:
                                    self.cards.append(player.cards.pop(i))
                                else:
                                    i += 1
                            return True
                        else:
                            print('Go fish!')
                            return False
            else:
                print("Player doesn't exist. Enter valid player name")

    def checkForGroups(self):
        cardNames = [card.name for card in self.cards]
        newFullGroupNames = []
        for cardName in cardNames:
            if cardName not in newFullGroupNames:
                if cardNames.count(cardName) == 4:
                    newFullGroupNames.append(cardName)
        if newFullGroupNames:
            i = 0
            while i < len(self.cards):
                if self.cards[i].name in newFullGroupNames:
                    self.cards.pop(i)
                else:
                    i += 1
            self.sets.extend(newFullGroupNames)

    def isStillPlaying(self):
        if len(self.cards) == 0:
            return False
        else:
            return True

import os

deck = Deck()
players = []
for i in range(1, 5):
    p = Player("Player " + str(i))
    for i in range(7):
        p.cards.append(deck.getTopCard())
    players.append(p)


gameRunning = True
turnCounter = -1
while gameRunning:
    os.system('clear')
    #decide which players turn it is and display their sets
    turnCounter += 1
    turnIndex = turnCounter % len(players)
    

    currentPlayer = players[turnIndex]
    input('Switch to player '+ currentPlayer.name)
    os.system('clear')
    print('Current Sets:', ', '.join(currentPlayer.sets))

    #start playing their turn
    stillPlaying = True
    while stillPlaying:
        cardRequested = currentPlayer.askForCard()
        stillPlaying = currentPlayer.askPlayerForCard(cardRequested, players)

    #go fish and check for groups/if they still have cards
    if len(deck.cards) > 0:
        currentPlayer.cards.append(deck.getTopCard()) #go fish
    currentPlayer.checkForGroups()
    gameRunning = currentPlayer.isStillPlaying()

#end game and display winner
os.system('clear')
maxPlayer = None
maxSets = 0
for player in players:
    if len(player.sets) > maxSets:
        maxPlayer = player
        maxSets = len(player.sets)
print(maxPlayer.name, 'has won with', maxSets, 'sets!')




        





