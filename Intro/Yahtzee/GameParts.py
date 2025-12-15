from random import randint
from time import sleep
import os

class Die:

    def __init__(self, sides):
        self.sides = sides
        self.value = randint(1, sides)

    def roll(self):
        self.value = randint(1, self.sides)

    def __str__(self):
        return str(self.value)

class Cup:

    def __init__(self):
        self.dice = []
        for i in range(5):
            self.dice.append(Die(6))

    def roll(self):
        res = []
        while len(self.dice) > 0:
            self.dice[0].roll()
            res.append(self.dice.pop(0))
        return res
    
class Player:

    def __init__(self, name):
        self.name = name
        self.cup = Cup()
        self.scoreBoard = Scoreboard()
        self.score = 0


    def doTurn(self):
        turnCount = 0
        rolledDice = []
        while turnCount < 3:
            rolledDice.extend(self.cup.roll())
            turnCount += 1

            reroll = False
            while reroll == False and turnCount < 3:
                os.system('cls')
                print(self.name)
                self.scoreBoard.print()

                rolledDiceValues = [str(die.value) for die in rolledDice]
                print('Dice to keep: ', ', '.join(rolledDiceValues))
                rerollDiceValues = [str(die.value) for die in self.cup.dice]
                print('Dice to reroll: ', ', '.join(rerollDiceValues))

                print('Enter the index of the dice you want to keep and press enter. Enter R to reroll')
                diceToKeep = input()
                if diceToKeep.isnumeric():
                    diceToKeep = int(diceToKeep) - 1
                    if diceToKeep < len(rolledDice):
                        self.cup.dice.append(rolledDice.pop(int(diceToKeep)))
                    else:
                        print("There aren't that many dice...")
                        sleep(3)
                else:
                    if diceToKeep.upper() == "R":
                        reroll = True
                    else:
                        print("Response not recognized...")
                        sleep(3)
        validSelection = False
        while not validSelection:
            os.system('cls')
            print(self.name + ': Choose which category by typing it')
            rolledDiceValues = [die.value for die in rolledDice]
            rolledDiceStrings = [str(die.value) for die in rolledDice]
            print('Dice to keep: ', ', '.join(rolledDiceStrings))
            self.scoreBoard.print()
            choice = input()
            validSelection = self.scoreBoard.addScore(rolledDiceValues, choice)
        self.cup = Cup()
        

    

class Scoreboard:

    def __init__(self):
        self.upper = {
            "Aces": 0,
            "Twos": 0,
            "Threes": 0,
            "Fours": 0,
            "Fives": 0,
            "Sixes": 0
        }
        self.lower = {
            "3 of a kind": 0,
            "4 of a kind": 0,
            "Full House": 0,
            "Small Straight": 0,
            "Large Straight": 0,
            "Yahtzee": 0,
            "Chance": 0
        }

    def print(self):
        upperC = list(self.upper.keys())
        lowerC = list(self.lower.keys())

        upperV = list(self.upper.values())
        lowerV = list(self.lower.values())

        for i in range(7):
            #add upper values
            string = ""
            if i < 6:
                string += upperC[i] + ":\t\t" + str(upperV[i])
                string += "\t\t" #add padding
                string += lowerC[i] + ":\t\t" + str(lowerV[i])
            else:
                string += "\t\t\t\t" + lowerC[i] + ":\t\t\t" + str(lowerV[i])
            print(string)

    
    def calcScore(self):
        total = 0

        #add up top scores and apply bonus if applicable
        for score in self.upper.values():
            total += score
        if total >= 63:
            total += 35

        #add up bottom scores
        for score in self.lower.values():
            total += score

        return total
    
    def addScore(self, dice, option):
        if option in self.upper:
            upperRecs = {
                "Aces": 1,
                "Twos": 2,
                "Threes": 3,
                "Fours": 4,
                "Fives": 5,
                "Sixes": 6
            }
            total = upperRecs[option] * dice.count(upperRecs[option])
            self.upper[option] = total
            return True
        if option in self.lower:
            if option == "3 of a kind":
                total = 0
                for i in range(1, 7):
                    if dice.count(i) >= 3:
                        softTotal = i * dice.count(i)
                        if softTotal >= total:
                            total = softTotal
                self.lower[option] = total
                return True
            if option == "4 of a kind":
                total = 0
                for i in range(1, 7):
                    if dice.count(i) >= 4:
                        softTotal = i * dice.count(i)
                        if softTotal >= total:
                            total = softTotal
                self.lower[option] = total
                return True
            if option == "Full House":
                hasTwo = False
                hasThree = False
                for i in range(1, 7):
                    if dice.count(i) == 2:
                        hasTwo = True
                    if dice.count(i) == 3:
                        hasThree = True
                if hasTwo and hasThree:
                    self.lower[option] = 25
                return True
            if option == "Small Straight":
                diceVals = list(set(dice))
                diceVals.sort()
                longestStreak = 0
                consecutiveCounter = 0
                lastVal = 0
                for die in diceVals:
                    if die == lastVal + 1:
                        consecutiveCounter += 1
                        if consecutiveCounter > longestStreak:
                            longestStreak = consecutiveCounter
                    else:
                        consecutiveCounter = 1
                    lastVal = die
                if longestStreak >= 4:
                    self.lower[option] = 25
                return True
            if option == "Large Straight":
                dice.sort()
                longestStreak = 0
                consecutiveCounter = 0
                lastVal = 0
                for die in dice:
                    if die == lastVal + 1:
                        consecutiveCounter += 1
                        if consecutiveCounter > longestStreak:
                            longestStreak = consecutiveCounter
                    else:
                        consecutiveCounter = 1
                    lastVal = die
                if longestStreak == 5:
                    self.lower[option] = 40
                return True
            if option == "Yahtzee":
                if dice.count(dice[0]) == 5:
                    self.lower[option] += 50
                return True
            if option == "Chance":
                total = 0
                for val in dice:
                    total += val
                self.lower[option] = total
                return True
    

        else:
            print("Response Not Recognized")
            sleep(3)
            return False


    