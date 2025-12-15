from random import randint

###a method to create a 100 x 100 array of three numbers between 0 and 100000 ex: [num1, num2, num3]
def getTestArray():
    SIZE = 200
    HIGHEST_VALUE = 100000
    res = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            cell = []
            for k in range(3):
                cell.append(randint(0, HIGHEST_VALUE))
            row.append(cell)
        res.append(row)
    return res





#Make a function based on the following contract:
#Name: findMaxIndexInColorArray
#Purpose: Print the row and column index of the brightest cell (largest sum), the most red cell, the most green cell, and the most blue cell
#Input: m x n array of color lists
#Output: Void
def findMaxIndexInColorArray(arr):
    winnerIndexes = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    biggestValues = [0,0,0,0]
    #index 0 is reddest
    #index 1 is greenest
    #index 2 is bluest
    #index 3 is brightest
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            cell = row[j]
            cellSum = 0
            for rgb in range(len(cell)):
                value = cell[rgb]
                cellSum += value
                if value > biggestValues[rgb]:
                    biggestValues[rgb] = value
                    winnerIndexes[rgb] = [i, j]
            if cellSum > biggestValues[3]:
                biggestValues[3] = cellSum
                winnerIndexes[3] = [i, j]
    labels = ["Reddest", "Greenest", "Blueest", "Brightest"]
    for i in range(len(labels)):
        print("The" , labels[i], "was row", winnerIndexes[i][0] , "column", winnerIndexes[i][1], "with a value of", biggestValues[i])

#write a program that:
#Creates a test array using the given function
#uses the findMaxIndexInColorArray function to print the row and column index of the brightest cell, most red cell, most green cell, and most blue cell
#CHALLENGE: if there's more than one cell that satisfies the requirement, list them all
testArray = getTestArray()
findMaxIndexInColorArray(testArray)