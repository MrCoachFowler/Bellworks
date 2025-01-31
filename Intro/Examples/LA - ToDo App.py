toDo = {
  'Sunday': [],
  'Monday': [],
  'Tuesday': [],
  'Wednesday': [],
  'Thursday': [],
  'Friday': [],
  'Saturday': [],
}

request = input('Would you like to add, get or test to your playlist?')
if request == 'add':
    day = input('What day do you want to add to?')
    act = input('what do you want to add to that day?')
    if act not in toDo[day]:
        toDo[day].append(act)
    
    else:
        print("it's already in there")
   
if request == 'get':
    answer = input('What day would you like to check?')
    print(toDo[answer])

if request == 'test':
    for key in toDo:
        toDo[key].extend(['Drink water', 'brush teeth', 'Eat breakfast'])