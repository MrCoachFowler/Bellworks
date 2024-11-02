import random

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



deck = createNewShuffledDeck()

players = []
playerCount = int(input('how many players?'))
for i in range(playerCount):
    player = []
    players.append(player)

#deal the deck
counter = 0
while len(deck) > 0:
    playerFocusIndex = counter % len(players) #this works it's crazzzzzy
    card = deck.pop()
    players[playerFocusIndex].append(card)
    counter += 1

for player in players:
    print(player)
def gameHasBeenWon(players):
    #see if any player has all the cards
    for player in players:
        if len(player) == 52:
            return True
    return False

#start the game
while not gameHasBeenWon(players):
    cardsPlayed = []
    cardValues = []

    for playerHand in players:
        if len(playerHand) == 0:
            cardValues.append(0)
        else:
            card = playerHand.pop()
            cardsPlayed.append(card)
            cardValues.append(card[2])

    maxCard = max(cardValues)
    maxCardCount = cardValues.count(maxCard)

    if maxCardCount > 1:
        war = True
        
        while war:
            newCardsPlayed = []
            newCardValues = []
            winningPlayerIndices = []
            for i in range(len(cardValues)):
                if cardValues[i] == maxCard:
                    winningPlayerIndices.append(i)

            cardValues = []
            for i in range(len(players)):
                #see if player amongst winners
                if not i in winningPlayerIndices or len(players[i]) == 0:
                    cardValues.append(0)
                else:
                    for i in range(3):
                        if len(players[i]) >= 2:
                            cardsPlayed.append(players[i].pop())
                    card = players[i].pop()
                    cardsPlayed.append(card)
                    cardValues.append(card[2])

            maxCard = max(cardValues)
            maxCardCount = cardValues.count(maxCard)
            if maxCardCount == 1:
                #war over
                war = False
                winnerIndex = cardValues.index(maxCard)
                for card in cardsPlayed:
                    players[winnerIndex].append(card)

            
    else:
        winningPlayerIndex = cardValues.index(maxCard)
        for card in cardsPlayed:
            players[winningPlayerIndex].append(card)


    #compare top cards and give cards to the winner
    #if there is a tie, play war
    ##each contender puts three cards face down and draws one card

for i in range(len(players)):
    player = players[i]
    if len(player) == 52:
        print('player ' + str(i) + ' has won!')
