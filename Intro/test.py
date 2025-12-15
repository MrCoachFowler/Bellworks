base_ball_list = [
    [' X ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', ' X '],
    ['   ', '   ', ' X ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', ' X ', '   ']
]

def printBasebaseField(user_map):
    from colorama import Fore, Back, Style
    def stringOfSpaces(numSpaces):
        numSpaces = int(numSpaces)
        res = ''
        for i in range(numSpaces):
            res += ' '
        return res

    #outfield
    for i in range(5):
        print(Back.GREEN + stringOfSpaces(100) + Style.RESET_ALL)
    #second base
    print(Back.GREEN +stringOfSpaces(41) + Back.WHITE + Fore.LIGHTWHITE_EX + '|'.join(user_map[2]) + Back.GREEN + stringOfSpaces(40) + Style.RESET_ALL)
    #start of infield
    for i in range(6):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(10 + i * 8) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #start of inner diamond
    for i in range(6, 11):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.LIGHTRED_EX + stringOfSpaces(i * 8 - 38) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #first base, third base, and pitcher mound
    #ends: green1: 5, yellow1: 24, red: 42, yellow2: 24, green2 5
    #maprowWidth: 24
    print(Back.WHITE + Fore.BLACK + '|'.join(user_map[3]) +  Back.LIGHTYELLOW_EX + stringOfSpaces(10) + Back.LIGHTRED_EX + stringOfSpaces(18) + Back.WHITE + stringOfSpaces(6) +Back.LIGHTRED_EX + stringOfSpaces(18) + Back.LIGHTYELLOW_EX+ stringOfSpaces(10) + Back.WHITE + '|'.join(user_map[1]) +Style.RESET_ALL)
    #lower half of in field
    for i in range(10, 5, -1):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.LIGHTRED_EX + stringOfSpaces(i * 8 - 38) + Back.LIGHTYELLOW_EX + stringOfSpaces(24) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    for i in range(5, -1, -1):
        print(Back.GREEN + stringOfSpaces(45 - i * 4) + Back.LIGHTYELLOW_EX + stringOfSpaces(10 + i * 8) + Back.GREEN + stringOfSpaces(45 - i * 4) + Style.RESET_ALL)
    #home base
    print(Back.GREEN +stringOfSpaces(41) + Back.WHITE + Fore.LIGHTWHITE_EX + '|'.join(user_map[0]) + Back.GREEN + stringOfSpaces(40) + Style.RESET_ALL)
    for i in range(2):
        print(Back.GREEN + stringOfSpaces(100) + Style.RESET_ALL)
    
    


printBasebaseField(base_ball_list)