from classes import Deck, Player
import os
import time

def playerHasWonGame(players):
    for player in players:
        if player.boardSize == 0:
            return player
    return False

def playerHasWonRound(players):
    for player in players:
        if player.wonRound():
            return player
    return False

players = []

print("How many players are there?")
playerCount = int(input())

for i in range(playerCount):
    print("What is the name of player " + str(i + 1) + "?")
    name = input()
    players.append(Player(name))

turnCounter = 0
while not playerHasWonGame(players):
    #set up deck for round
    deck = Deck()
    deck.shuffle()
    for player in players:
        player.setUpBoards(deck)
    discard = deck.cards.pop(0)

    #play a round
    while not playerHasWonRound(players):
        os.system('cls')
        if len(deck.cards) < 5:
            deck = Deck()
            deck.shuffle()

        activePlayer = players[turnCounter % len(players)]

        print('it is ' + activePlayer.name + "'s turn!")
        print('You have: ')
        activePlayer.printBoard()

        cardToUse = activePlayer.decideDrawOrDiscard(discard, deck)
        while cardToUse:
            discard = cardToUse
            cardToUse = activePlayer.replaceCard(cardToUse)

        print("After your turn, you now have...")
        activePlayer.printBoard()
        time.sleep(3)

        turnCounter += 1

    activePlayer.boardSize -= 1
    print(activePlayer.name + " has won the round! Only " + str(activePlayer.boardSize) + " cards now...")
    if activePlayer.boardSize == 0:
        print("Game over! " + activePlayer.name + " has won")
    time.sleep(3)
        

    

