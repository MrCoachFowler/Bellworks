from random import randint
import datetime
#Make a function based on the following contract:
#Name: luckMeter
#Purpose: Generate random numbers between 1 and a specified number and time how long it takes to find a number under 10
#Input: maxNumber of guesses
#Output: time taken to get a random number equal to or under 10

#mr_fowler: to get the current date and time, use something like tic = datetime.datetime.now()
#mr_fowler: to get the difference between two datetimes in seconds, use:
#mr_fowler: duration = toc - tic
#mr_fowler: timeInSeconds = duration.seconds

#write a program that:
#prints how long it takes if the maxnum is 100
#prints how long it takes if the max num is 100000000
#prints how long it takes if the max num is 1000000000