import random
from os import system
from colorama import Fore

#name: makeDeck
#purpose: create a standard 52 card deck
#inputs: void
#outputs: deck (a list of lists containing the suite and a value)
##2 card example: [ ['Spade', '4'], ['Heart', 'Q'] ]

def makeDeck():
    suits = ['Red', 'Blue', 'Yellow', 'Green']
    names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Draw Two', 'Skip', 'Reverse']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0]

    #initialize the deck variable (output variable)
    deck = []

    #for every suit...
    for suit in suits:
        #for every value in that suit...
        for i in range(len(names)):
            name = names[i]
            value = values[i]
            #add a new "card" to the deck of that suit and value
            deck.append([suit, name, value])

    #add wilds
    names = ['Wild', 'Wild Draw Four']
    #add two of each
    for i in range(2):
        for name in names:
            deck.append([None, name, 0])

    return deck

#name: shuffleDeck
#purpose: Take in a deck and shuffle it
#input: deck to shuffle
#output: the same deck but ~shuffled~
def shuffleDeck(deck):
    shuffledDeck = []
    #Remove a random card from deck and put it in shuffled
    while len(deck) > 0:
        randCardIndex = random.randint(0, len(deck) - 1)
        randCard = deck.pop(randCardIndex)
        shuffledDeck.append(randCard)

    return shuffledDeck

def createNewShuffledDeck():
    deck = makeDeck()
    deck = shuffleDeck(deck)

    return deck

def printCard(card):
    if card[0] == "Green":
        print(Fore.GREEN + str(card) + Fore.RESET)
    elif card[0] == "Blue":
        print(Fore.BLUE + str(card) + Fore.RESET)
    elif card[0] == "Red":
        print(Fore.RED + str(card) + Fore.RESET)
    elif card[0] == "Yellow":
        print(Fore.YELLOW + str(card) + Fore.RESET)
    else:
        print(card)


deck = createNewShuffledDeck()
for card in deck:
    printCard(card)


#get number of players
playerCount = int(input('How many players are there?'))
system('cls')
#give players 7 cards to start
players = []
for i in range(playerCount):
    players.append([])
    for j in range(7):
        players[i].append(deck.pop(0))
#add a card to the discard pile to start
lastDiscard = deck.pop(0)
#start game
keepPlaying = True
turnIncrementor = 0
while keepPlaying:
    #keep track of if reversed or not
    isReverse = False
    #have players play their turn
    #if player is out, set keep playing to false and break the loop
    activePlayerHand = players[ turnIncrementor % len(players)] #this works, trust me
    for card in activePlayerHand:
        print()

    

