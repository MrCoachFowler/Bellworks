import os

weeklyToDoList = {}

daysOfTheWeek = [
'Monday',
'Tuesday',
'Wednesday',
'Thursday',
'Friday',
'Saturday',
'Sunday',
]

for days in daysOfTheWeek:
    weeklyToDoList[days] = []

def addToDay(day, tasks):
    splitTasks = tasks.split(', ')
    if tasks in weeklyToDoList[day]:
        print('That task is already in your to do list for that day')
    else:
        weeklyToDoList.get(day).extend(splitTasks)
    return weeklyToDoList


def getDayOfTheWeek(chosenDay):
    print(weeklyToDoList.get(chosenDay))


def testDayOfTheWeek():
    exampleActs = ['Brush teeth', 'Drink water', 'Eat Breakfast']
    for days in weeklyToDoList:
        weeklyToDoList.get(days).append(exampleActs)
    return weeklyToDoList

while 1 == True:
    print('''Would you like to:
    1. Add (Adds to a day's to do list)
    2. Get (Prints a day's to do list)
    3. Test (Adds Brush teeth, Drink water, Eat Breakfast to every days' to do list)
    ''')
    playerInput = input('Choose an action: ')       
    if playerInput == '1':
        addToDay(input('Which day would you like to add tasks to? '), input('What tasks do you need to add? (You can add multiple tasks by seperating them with ", ") '))
    elif playerInput == '2':
        getDayOfTheWeek(input("Which day's tasks would you like to see? "))
    elif playerInput == '3':
        testDayOfTheWeek()
    else:
        print("I'm sorry, I don't know that option")