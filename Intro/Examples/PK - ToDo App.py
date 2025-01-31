toDoList = {}
daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

while True:
    whatToDo = input("What would you like to do? (add, get, or test) ").lower()
    if whatToDo == 'add':
        whenToAdd = input("What day of the week would you like to add to? ")
        if whenToAdd in daysOfWeek:
            if whenToAdd in toDoList:
                whatToAdd = input(f"What would you like to add to {whenToAdd}. ")
                if whatToAdd in toDoList[whenToAdd]:
                    print("That is already in the toDo list for that day.")
                else:
                    toDoList[whenToAdd] += whatToAdd
        else:
            print("That is not a valid day of the week.")

    elif whatToDo == 'get':
        whenToGet = input("What day of the week would you like to see? ")
        if whenToGet in toDoList.keys():
            print(toDoList[whenToGet])
        else:
            print(f"{whenToGet} is either empty or not in the toDo list.")

    elif whatToDo == 'test':
        for day in daysOfWeek:
            toDoList[day] = ["brush teeth", "drink water", "eat breakfast"]

    elif whatToDo == 'q' or whatToDo == 'quit':
        print("Quitting...")
        break

    else:
        print(f"{whatToDo} is not an accepted input.")