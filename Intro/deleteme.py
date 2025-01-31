import random
import os
game = True
Running = True


#inputs: void
#outputs: deck (a list of lists containing the suite and a value)

def makeDeck():
    suits = ['Heart', 'Spade', 'Diamond', 'Club']
    names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',  'K']
    values =[ 14,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ,  10 ,  11,  12,  13]
    #initialize the deck variable (output variable)
    deck = []

    #for every suit...
    for suit in suits:
        for i in range(len(names)):
            name = names[i]
            value = values[i] 
            #add a new "card" to the deck of that suit and value
            deck.append([suit, name, value])

    return deck

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

def split_deck_between_two(deck):
    
    p1 = [] 
    p2 = []

    #Here my code is assigning each player cards
    for card in deck:
        while len(deck) < 26:
            p1.append(card)
        else:
            p2.append(card)
    return p1, p2 
os.system('cls') #I'm trying to make the screen more visually appealing instead of overloading them with every card's value so I did "os.system('cls')".

def createNewShuffledDeck():
    deck = makeDeck()
    deck = shuffleDeck(deck)

    return deck

deck = createNewShuffledDeck()
p1, p2 = split_deck_between_two(deck)
print ("Player 1's deck", p1)
print ("Player 2's deck", p2)
os.system('cls') #I'm trying to make the screen more visually appealing instead of overloading them with every card's value so I did "os.system('cls')".

deck = createNewShuffledDeck()
print(deck)

while Running:  #This is where the main game occurs; players drawing hands and comparing values along with who won the round (Where the magic happens)
    
    p1 = []
    p2 = []
    for i in range(52):
        if i % 2 == 0:
            p1.append(deck[i])
        else:
            p2.append(deck[i])
    p1_hand = p1.pop()  #Here is where I tried to make a function that would pick a card out of both players deck and comapre them
    p2_hand = p2.pop()  

    print("Player 1's card is...", p1_hand)
    print("Player 2's card is...", p2_hand)
    
    if p1_hand[2] > p2_hand[2]:   #Here is where the values are compared
        print("Player 1 has the superior card and is victorious this round")
    elif p1_hand[2] < p2_hand[2]:
        print("Player 2 has the superior card and is victorious this round")
    else:
        print("Player 1 and 2 have tied... onto the next round...")

    input('Press Enter to continue to the next round friend :) ')
    os.system('cls')  

        #function to declare the winner
    if len(p1) == 0:
        print("Player 2 wins the game!")
        Running = False
    elif len(p2) == 0:
        print("Player 1 wins the game!")