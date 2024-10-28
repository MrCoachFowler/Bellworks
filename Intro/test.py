import datetime
from time import sleep

def getCurrentDateTime():
    rightNow = datetime.datetime.now()
    return rightNow

tic = getCurrentDateTime()
sleep(3)
toc = getCurrentDateTime()

timeDiff = toc - tic
microSecondDiff = timeDiff.microseconds * .000001
secondDiff = timeDiff.seconds
print('time change is: ' + str(secondDiff + microSecondDiff))

