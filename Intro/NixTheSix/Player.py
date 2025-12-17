#A class to create player objects from
# Each player has a name, list of Die objects, and a score
# Player should be able to:
#     Get a new set of five dice
#     Check to see if any of their dice are sixes
#     Add all their dice together
#     Play a turn requiring them to roll and reroll until there are no sixes, then add the dice total of the roll to their score
from Die import Die


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice = []

    def startRound(self):
        self.dice = []
        while(len(self.dice) < 5):
            self.dice.append(Die())
        print("It's " + self.name + "'s turn!!")
        input('Hit enter for the first roll...')

    def rollDice(self):
        for die in self.dice:
            die.roll()

    def hasSixDie(self):
        hasSixes = False
        i = 0
        while i < len(self.dice):
            die = self.dice[i]
            if die.value == 6:
                hasSixes = True
                self.dice.pop(i)
            else:
                i += 1
        return hasSixes
    
    def getDiceTotal(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    def printDiceValues(self):
        diceString = ''
        for die in self.dice:
            diceString += str(die.value) + ' ' 
        print(diceString)

    def playTurn(self):
        self.startRound()
        self.rollDice()
        self.printDiceValues()
        while self.hasSixDie():
            input('A six! Hit enter to reroll...')
            self.rollDice()
            self.printDiceValues()
        roundTotal = self.getDiceTotal()
        if len(self.dice) > 0: print('No sixes!! Well done. This earned a score of ' + str(roundTotal))
        else: print('Aww, tough luck. Zero points for this round')
        self.score += roundTotal
        input('Hit enter to go to the next person')

                