
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