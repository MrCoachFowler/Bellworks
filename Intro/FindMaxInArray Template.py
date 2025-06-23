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


#write a program that:
#Creates a test array using the given function
#uses the findMaxIndexInColorArray function to print the row and column index of the brightest cell, most red cell, most green cell, and most blue cell
#CHALLENGE: if there's more than one cell that satisfies the requirement, list them all
