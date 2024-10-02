import os
# playing = True
# while playing == True:

# FLOOR LISTS

# all floors
castle = [[], [], [], [], []]
castle[0] = [[], []] # floor 0, tutorial
castle[1] = [[], [], []] # floor 1,
castle[2] = [[], [], [], []] # floor 2,
castle[3] = [[], [], [], []] # Floor 3,
castle[4] = [[]]  # floor 4, the king


# zero floor
castle[0][0] = ["Here's the staircase into the castle, c'mon. ", "staircase up" ]
castle[0][1] = ["There's nothing here, just Mr. Frog. Keep going. ", "nothing"]
# first floor
castle[1][0] = ["There's two staircases going up and down out the castle, but don't be a coward, keep going! ", "staircase up", "staircase down"] # where the player starts
castle[1][1] = ["Theres a dagger in here, what will you do? ", "dagger"]
castle[1][2] = ["A locked chest, strange. ", "chest"]
# second floor
castle[2][0] = ["Just a staircase down, keep going. ", "staircase down"]
castle[2][1] = ["Oh no, a kinight! What will you do? ", "knight"]
castle[2][2] = ["An armour room, oh wow. What will you do? ", "armor"]
castle[2][3] = ["Here's the staircase, go! ", "staircase up"]
# thrid floor
castle[3][0] = ["Just a staircase down, keep going. ", "staircase down"]
castle[3][1] = ["A knight is blocking the next room, what will you do? ", "knight"]
castle[3][2] = ["There is a mysterious key on the floor, how odd ", "key"]
castle[3][3] = ["A night is blocking the final staircase, what will you do? ", "knight", "staircase up"]
# fourth floor
castle[4][0] = ["The final floor. "]

#mr_fowler: you'll need to make the rest, but you might want a short description of each room for each
castleDescriptions = [[], [], [], [], []]
castleDescriptions[0] = [[], []] # floor 0, tutorial
castleDescriptions[1] = [[], [], []] # floor 1,
castleDescriptions[2] = [[], [], [], []] # floor 2,
castleDescriptions[3] = [[], [], [], []] # Floor 3,
castleDescriptions[4] = [[]]  # floor 4, the king

castleDescriptions[0][0] = "Entry"
castleDescriptions[0][1] = "Hallway"


# MAP BOARDS 
# (all the room icons are suppose to be just blank spaces but theyre random numbers and such for testing reasons)

#mr_fowler: make these functions which return your function string (which is super cool!)
##by passing the rooms as an input, we can move away from keeping track of a bunch of variables
def floor_4_map(rooms):
    return ("_________________________________________________________________\n"
    "|               |               |               |               |\n"
    "|               |               |               |               |\n"
    "|               |               |               |               |\n"
    "|       " + rooms[0] + "         /     " + rooms[1] + "         /     " + rooms[2] + "         /     " + rooms[3] + "        |\n"
    "|               |               |               |               |\n"
    "|               |               |               |               |\n"
    "|_______________|_______________|_______________|_______________|\n")

def floor_3_map(rooms):
    result = ("_________________________________________________\n"
    "|               |               |               |\n"
    "|               |               |               |\n"
    "|               |               |               |\n"
    "|       " + rooms[0] + "        /      " + rooms[1] + "        /      " + rooms[2] + "       |\n"
    "|               |               |               |\n"
    "|               |               |               |\n"
    "|_______________|_______________|_______________|\n")
    return result

def floor_2_map(rooms):
    result = ("___           ______          ___\n"
    "|               |               |\n"
    "\n"
    "\n"
    "     " + rooms[0] + "          " + rooms[1] + "\n"
    "\n"
    "\n"
    "|__          ___|___          __|\n")
    return result



os.system('cls')

# first = input("YOU ARE (name here idk) \n" + "YOU NEED TO SLAY THE KING \n" + "YOU WOULD MAKE A MUCH BETTER KING THAN HIM \n" + "(Press enter to continue) ")
# os.system('cls')




player_inventory = []
player_map = "" #mr_fowler: reset the player map each turn
player_room = 0
player_floor = 0 #mr_fowler: you might want to start on the first floor (zero index)
game = "on"
#mr_fowler: the number of rooms is variable which is tough, so nice.
##by using a loop to move through, you can add a variable amount of things
roomCounter = 0
map_rooms = []
while roomCounter < len(castle[player_floor]):
    map_rooms.append(castleDescriptions[player_floor][roomCounter])
    roomCounter += 1

while game == "on":
    if player_floor == 2 or player_floor == 3:
        print("this has four rooms")
        player_map = floor_4_map(map_rooms)
    elif player_floor == 1:
        print("this has three rooms")
        player_map = floor_3_map(map_rooms)
    elif player_floor == 0:
        print("this has two rooms")
        player_map = floor_2_map(map_rooms)
   
    #map_rooms[player_room] = "■ test" #mr_fowler: idk what this is...

    print(player_map)
    room = castle[player_floor][player_room]
    # print(player_floor, player_room)
    action = input(room[0])
    os.system('cls')
   
    # QUIT
    if action == "q":
        game = "2763"

# ROOM CHECKS -------------------------------------

    # KNIGHT
    if "knight" in castle[player_floor][player_room]:
        if action == "a" or action == "attack":
            if "dagger" in player_inventory:
                print("You've slain the knight!! Good job.")
                castle[player_floor][player_room].remove("knight")
                if "staircase up" in castle[player_floor][player_room]:
                    castle[player_floor][player_room][0] = "Don't let the deceast knight distract you, contunue onwards up the stairs! "
                elif "staircase down" in castle[player_floor][player_room]:
                    castle[player_floor][player_room][0] = "Just the leftover armor of the knight and the staircase back down, go on. "
                else:
                    castle[player_floor][player_room][0] = "Nothing here anymore. "
            else:
                print("You don't have a weapon!! \nThe knight has slain you, your whole journey has been for naught.. \nYOU DIED.")
                game = "2763"
        else:
            print("You tried avoiding the knight but that gave them an opportunity to attack you. \nThe knight has slain you, your whole journey has been for naught.. \nYOU DIED.")
            game = "2763"

   
# ACTION CHECKS ----------------------------------
   
    # FORWARD
    if action == "f":
        if player_room != len(castle[player_floor]) -1:
            player_room += 1
            if player_room > len(castle[player_floor]) -1:
                player_floor += 1
                player_room = 0
                room = castle[player_floor][player_room]
            room = castle[player_floor][player_room]
        else:
            print("There is no other door here")

    # BACKWARDS
    if action == "b":
        if player_room != 0:
            player_room -= 1
        else:
            print("You cant go back any further, be brave and carry on!")
        room = castle[player_floor][player_room]
    room = castle[player_floor][player_room]

    # UP
    if action == "u" or action == "up":
        if "staircase up" in castle[player_floor][player_room]:
            if player_floor == 2 and player_room == 3:
                player_floor = 3
                player_room = 0
            elif player_floor == 3 and player_room == 3:
                player_floor = 4
                player_room = 0
            else:
                player_floor += 1  
        else:
            print("Nuh uh you cant do that, there's no stairs")

    # DOWN
    if action == "d" or action == "down":
        if "staircase down" in castle[player_floor][player_room]:
            player_floor -= 1  
        else:
            print("Nuh uh you cant do that, there's no stairs")

    # GRAB
    if action == "g" or action == "grab":
        if "key" in castle[player_floor][player_room] or "armor" in castle[player_floor][player_room] or "dagger" in castle[player_floor][player_room]:
            new_item = castle[player_floor][player_room].pop(1)  
            player_inventory.append(new_item)
            print(player_inventory)
            cont = input("You grabbed a " + new_item + '! Type "i" to see your current inventory ')
            castle[player_floor][player_room][0] = "Nothing here anymore. "
           
    # INTERACT
    if action == "i" or action == "interact":
        if "chest" in castle[player_floor][player_room]:
            if "key" in player_inventory:
                print("You opened the chest to reveal a whoaaa cool, congradulations!!!")
                player_inventory.append("whoaaaa cool")
                castle[player_floor][player_room][0] = "Just an empty chest now. "
                castle[player_floor][player_room][1] = "nothing"
                player_inventory.remove("key")
        print("Interact with what??? Just keep going. ")