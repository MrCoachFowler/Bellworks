import datetime

#Make a function based on the following contract:
#Name: timer
#Purpose: record the time difference between a user hitting enter
#Input: none
#Output: time it took
def timer():
    print('hit enter twice quickly and see how fast you did it!')
    input('hit enter to start')
    tic = datetime.datetime.now()
    input('hit enter to stop')
    toc = datetime.datetime.now()
    duration = toc - tic
    return duration.microseconds / 1000

#write a program that:
#tells a user how quickly they pressed enter
#tells a user they are fast if it is under 100 milliseconds and slow if above (if exactly 50, call them a wizard!)

timeTaken = timer()
print('time taken: ' + str(timeTaken))
if(timeTaken < 100):
    print('you are fast!')
elif timeTaken == 100:
    print('you are a wizard!')
else:
    print('maybe a little faster next time..')