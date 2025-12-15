<<<<<<< HEAD

def getDeckOrDiscard(self, topDiscard, deck):
    print('Do you want the discard, ' + topDiscard.value + ', or draw from the deck?')
    print('Enter 1 for discard\nEnter 2 for deck')
    decision = input()
    if decision == "1":
        return topDiscard
    else:
        return deck.cards.pop(0)

def replaceCards(self, newCard):
    #see if the new card can be played. Then get the card that was on the board in its place
    #repeat this until the new card can no longer be played then return it as the discard
    while True:
        #verify the new card can be played
        ##face cards don't count
        if newCard.value in ['J', 'Q', 'K']:
            return newCard
        ##now that it's not a face card, let's get its index. We're going to use its value minus one except for A.
        ##since A is the only non number card left, we can identify the special case and know its index is zero.
        cardIndex = -1
        if not newCard.value.isdigit():
            cardIndex = 0
        else:
            ##identify its index from its value
            cardValNum = int(newCard.value)
            cardIndex = cardValNum - 1

        #check to see if the index is even on the users board (if they have 8 cards, they don't need a 10). If not, return newcard for discard
        indexOnBoard = cardIndex < self.boardSize
        if not indexOnBoard:
            return newCard

        #check to see if they haven't played that card, else return the newcard as discard
        cardNotPlayed = self.showBoard[cardIndex] == '| x |'
        if cardNotPlayed:
            #replace the card in showboard and set the card laying there to be the new card
            self.showBoard[cardIndex] = '| ' + newCard.value + ' |'
            newCard = self.board[cardIndex]
        else:
            return newCard
=======
base_ball_list = [
    [' X ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', ' X '],
    ['   ', '   ', ' X ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', ' X ', '   ']
]

def printBasebaseField(user_map):
    from colorama import Fore, Back, Style
    def stringOfSpaces(numSpaces):
        numSpaces = int(numSpaces)
        res = ''
        for i in range(numSpaces):
            res += ' '
        return res

    #outfield
    for i in range(5):
        print(Back.GREEN + stringOfSpaces(100) + Style.RESET_ALL)
    #second base
    print(Back.GREEN +stringOfSpaces(41) + Back.WHITE + Fore.LIGHTWHITE_EX + '|'.join(user_map[2]) + Back.GREEN + stringOfSpaces(40) + Style.RESET_ALL)
    #start of infield
    for i in range(6):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(10 + i * 8) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #start of inner diamond
    for i in range(6, 11):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.LIGHTRED_EX + stringOfSpaces(i * 8 - 38) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #first base, third base, and pitcher mound
    #ends: green1: 5, yellow1: 24, red: 42, yellow2: 24, green2 5
    #maprowWidth: 24
    print(Back.WHITE + Fore.BLACK + '|'.join(user_map[3]) +  Back.LIGHTYELLOW_EX + stringOfSpaces(10) + Back.LIGHTRED_EX + stringOfSpaces(18) + Back.WHITE + stringOfSpaces(6) +Back.LIGHTRED_EX + stringOfSpaces(18) + Back.LIGHTYELLOW_EX+ stringOfSpaces(10) + Back.WHITE + '|'.join(user_map[1]) +Style.RESET_ALL)
    #lower half of in field
    for i in range(10, 5, -1):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.LIGHTRED_EX + stringOfSpaces(i * 8 - 38) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    for i in range(5, -1, -1):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(10 + i * 8) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #home base
    print(Back.GREEN +stringOfSpaces(41) + Back.WHITE + Fore.LIGHTWHITE_EX + '|'.join(user_map[0]) + Back.GREEN + stringOfSpaces(40) + Style.RESET_ALL)
    for i in range(2):
        print(Back.GREEN + stringOfSpaces(100) + Style.RESET_ALL)
    
    


printBasebaseField(base_ball_list)
>>>>>>> e0a5c590761ea29fd67c4ac8c762aea63c42de47
