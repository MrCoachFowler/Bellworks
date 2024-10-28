from random import randint
import datetime
#Make a function based on the following contract:
#Name: luckMeter
#Purpose: Generate random numbers between 1 and a specified number and time how long it takes to find a number under 10
#Input: maxNumber of guesses
#Output: time taken to get a random number equal to or under 10
def luckMeter(maxNum):
    tic = datetime.datetime.now()
    gotLucky = False
    while not gotLucky:
        randNum = randint(1, maxNum)
        if randNum <= 10:
            toc = datetime.datetime.now()
            gotLucky = True
    timeTaken = toc - tic
    return timeTaken.seconds

#write a program that:
#prints how long it takes if the maxnum is 100
#prints how long it takes if the max num is 100000000
#prints how long it takes if the max num is 1000000000
print('out of 100')
print(luckMeter(100))

print('out of 100000000')
print(luckMeter(100000000))

print('out of 1000000000')
print(luckMeter(1000000000))