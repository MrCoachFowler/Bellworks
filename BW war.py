import os
import random

#name: makeDeck
#purpose: create a standard 52 card deck
#inputs: void
#outputs: deck (a list of lists containing the suite and a value)
##2 card example: [ ['Spade', '4'], ['Heart', 'Q'] ]

def makeDeck():
    suits = ['Heart', 'Spade', 'Diamond', 'Club']
    names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen','King']
    values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    #initialize the deck variable (output variable)
    deck = []

    #for every suit...
    for suit in suits:
        #for every value in that suit...
        for i in range(len(names)):
            #add a new "card" to the deck of that suit and value
            name = names[i]
            value = values[i]
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

def hand_out_cards(deck):

    loop = 0
    player1 = []
    player2 = []
    for card in deck:
        turn = loop % 2
        if turn == 0:
            player1.append(card)
        elif turn == 1:
            player2.append(card)
        loop += 1
    return player1, player2


deck = createNewShuffledDeck()
# print(deck)
player1, player2 = hand_out_cards(deck)


# cont = input("Press enter to begin the game ")

# print(player1)
# print(player2)

# print(player1[2])

# loop = 0
# while loop < 10:
#     turn = loop % 2
#     print(turn)
#     loop += 1

#     if turn == 0:
#         print("Its player one's turn")
#     elif turn == 1:
#         print("It is player two's turn") 

def print_cards_played(player, card1):
    if card1[1] == "A" or card1[1] == 8 or card1[1] == 11:
        a_or_an = "an"
    else:
        a_or_an = "a"

    if player == player1:
        player_num = "1"
    elif player == player2:
        player_num = "2"
    
    print("Player", player_num, "placed", a_or_an, card1[1], "of", card1[0] + "s")

# print_cards_played(player1, player1[0])

def play_cards(player1, player2):
    cards_out = True
    while cards_out == True:
        # print_cards_played(player1, player1[0])
        # print_cards_played(player2, player2[0])
        
        player1card = player1.pop(0)
        player2card = player2.pop(0)
        print(player1card)
        print(player2card)

        print(len(player1), len(player2))

        if player1card[2] == player2card[2]:
            # print(player1card[0, 1])
            print("A tie")
            player1.append(player1card)
            player2.append(player2card)
            # cont = input("(enter to continue)")

        elif player2card[2] < player1card[2]:
            player1.append(player1card)
            player1.append(player2card)
            print("Player 1 won this round")
            cards_out = False
    
        elif player1card[2] < player2card[2]:
            player2.append(player2card)
            player2.append(player1card)
            print("Player 2 won this round")
            cards_out = False
        
    return player1, player2

counter = 0
while player1 != [] and player2 != []:
    counter += 1
    print('player 1: ')
    print(player1)
    print('player 2:')
    print(player2)
    play_cards(player1, player2)

    # if counter > 26:
    #     break


    if len(player1) == 0:
        print("Player 2 won!!")
    elif len(player2) == 0:
        print("Player 1 won!!")


# print("PLAYER 1: ", player1)
# print("PLAYER 2: ", player2)

# play_cards()

# print("PLAYER 1: ", player1)
# print("PLAYER 2: ", player2)