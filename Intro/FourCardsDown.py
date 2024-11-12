import random
from matplotlib import pyplot

#name: makeDeck
#purpose: create a standard 52 card deck
#inputs: void
#outputs: deck (a list of lists containing the suite and a value)
##2 card example: [ ['Spade', '4'], ['Heart', 'Q'] ]

def makeDeck():
    suits = ['Heart', 'Spade', 'Diamond', 'Club']
    names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K']
    values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

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

keepPlaying = True
playerCount = int(input('how many players are there?'))
playerScores = [0] * playerCount

while keepPlaying:
    #refresh the deck
    deck = createNewShuffledDeck()

    #make a list of all players and give them their four cards
    players = []
    for i in range(playerCount):
        playerHand = []
        for j in range(4):
            playerHand.append(deck.pop(0))
        players.append(playerHand)
    
    #allow players to see their end cards
    for i in range(players):
        playerHand = players[i]
        input('player ' + str(i + 1) + ' hit enter to see your end cards')
        print(str(playerHand[0][1]) + ' | x | | x | ' + str(playerHand[3][1]))
        
    #start playing rounds
    knocked = False
    