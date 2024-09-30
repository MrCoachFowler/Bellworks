import random

#Make a function based on the following contract:
#Name: countDucks
#Purpose: Create a string of "duck" of varying lengths
#Input: number of ducks to count to (int)
#Output: string
def countDucks(duckNum):
    #if duckNum less than one, return empty string
    if(duckNum < 1):
        return ""
    
    #start with one duck
    #add the next ducks with a space before
    result = "duck"
    counter = 1
    while counter < duckNum:
        result += " duck"
        counter += 1

    return result

#write a program that:
#prints three rounds of duck, duck goose where the number of ducks is a random number between 6 and 12
roundCounter = 0
while roundCounter < 3:
    roundCounter += 1
    ducks = countDucks(random.randint(6,12))
    fullGame = ducks + " goose!"
    print(fullGame)