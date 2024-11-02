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



deck = createNewShuffledDeck()

playerNames = []
players = []
playerCardCounts = {}
playerCount = int(input('how many players?'))
for i in range(playerCount):
    player = []
    players.append(player)
    playerName = "Player " + str(i + 1)
    playerNames.append(playerName)

#deal the deck
counter = 0
while len(deck) > 0:
    playerFocusIndex = counter % len(players) #this works it's crazzzzzy
    card = deck.pop()
    players[playerFocusIndex].append(card)
    counter += 1

# for player in players:
#     print(player)

#add the first card counter to the dictionary
for i in range(len(players)):
    playerName = playerNames[i]
    player = players[i]
    playerCardCounts[playerName] = [len(player)]

#start the game
while len(players) > 1:
    cardsPlayed = []
    cardValues = []

    #have each player play a card
    for player in players:
        card = player.pop(0)
        cardsPlayed.append(card)
        cardValues.append(card[2])

    #See if there is a war
    maxValue = max(cardValues)
    isWar = cardValues.count(maxValue) > 1

    if not isWar:
        #find winning players index
        #award player at that index all the cards played
        #reset played card values and played cards
        winnerIndex = cardValues.index(maxValue)
        for card in cardsPlayed:
            players[winnerIndex].append(card)
        cardsPlayed = []
        cardValues = []

    else:
        #continue the war until it stops
        while isWar and len(players) > 1:
            #identify all winners
            winnerIndices = []
            for i in range(len(players)):
                if cardValues[i] == maxValue:
                    winnerIndices.append(i)

            #reset card values and play war
            cardValues = []
            for i in range(len(players)):
                if i in winnerIndices:
                    #This player is in the war. Play their hand
                    player = players[i]
        
                    #if the player has enough cards
                    if len(player) >= 4:
                        #draw three
                        for i in range(3):
                            card = player.pop(0)
                            cardsPlayed.append(card)
                        #draw and use the fourth
                        card = player.pop(0)
                        cardsPlayed.append(card)
                        cardValues.append(card[2])
                    elif len(player) > 0:
                        #take their last card and add the rest to cards played
                        card = player.pop(-1)
                        cardsPlayed.append(card)
                        cardValues.append(card[2])
                        for card in player:
                            cardsPlayed.append(player.pop(0))
                    else:
                        cardValues.append(0)
                else:
                    #this player not in the war
                    cardValues.append(0)

            maxValue = max(cardValues)
            #if there is one winner, award the cards and end the war. Otherwise continue war
            # print('players:')
            # for player in players:
            #     print(player)
            # print(cardValues)
            # print(maxValue)
            if cardValues.count(maxValue) == 1:
                winningIndex = cardValues.index(maxValue)
                # print(winningIndex)
                for card in cardsPlayed:
                    players[winningIndex].append(card)
                isWar = False
                cardValues = []
                cardsPlayed = []
                
    #keep track of how many cards each player has
    for i in range(len(players)):
        playerCardCounts[playerNames[i]].append(len(players[i]))

    
    #remove players who have no cards
    i = 0
    while i < len(players):
        #if player has no cards, remove them then continue at current index. otherwise check next players
        if len(players[i]) == 0:
            players.pop(i)
            playerNames.pop(i)
        else:
            i += 1
        

print(playerNames[0] + " wins!")
# for player in playerCardCounts:
#     print(playerCardCounts[player])

#make graph
turnCounter = []
maxTurn = 0
for player in playerCardCounts:
    playerLastTurn = len(playerCardCounts[player])
    if playerLastTurn > maxTurn:
        maxTurn = playerLastTurn
for turn in range(maxTurn):
    turnName = turn + 1
    turnCounter.append(turnName)

for player in playerCardCounts:
    cardCount = playerCardCounts[player]
    while len(cardCount) < len(turnCounter):
        cardCount.append(0)
    pyplot.plot(turnCounter,cardCount)

pyplot.show()
