week_days = {}
days_of_week=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
while True:
    print('''Options for your to-do list: 
            Get
            Add
            Test
            Finish''')
    print('.')
    options=input('Would you like to do?').lower()
    if options=='get':
        day=input('Which day would you like to see?').lower()
        if day in week_days:
            print(day,':', week_days[day])
        else:
            print('Nothing has been added to that day yet')
    elif options=='add':
        day=input('Which day would you like to update?').lower()
        if day in week_days:
            item=input('What item would like to add to that day?')
            if item in week_days[day]: 
                print('That item has already been added')
            else:
                week_days[day].append(item)
        else:
            week_days[day]=[]
            item=input('What item would like to add to that day?')
            if item in week_days[day]: 
                print('That item has already been added')
            else:
                week_days[day].append(item)

           
    elif options=='test': 
        for day in days_of_week:
            if day not in week_days:
                    week_days[day]=['brush teeth', 'eat brekfast', 'drink water']
        
            else:
                for day in week_days:
                    week_days[day].append('brush teeth')
                    week_days[day].append('eat brekfast')
                    week_days[day].append('drink water')
          
                    
    elif options=='finish':
        print('You have finished updating your To-Do list')
        break