import os
import time 



input('Alex Adams is a world renowned dungeon diver. He has explored all the most mysterious and dangerous dungeons in the world. After he had reached all locations there was only one question people wanted to know. Could he be the first person to pass through the Dungeon of Death and live? On Friday the 13th, he decided to make an attempt at the worlds most dangerous dungeon. Press enter to continue.')

plyrInventory = []
plyrFloor = 0
plyrRoom = 0
plyrLocation = 0
previousRoom = -1
finalMonsterEliminated = False
surived = False
playerMove=0
dungeonLayout= [
    ['__X__','_____','_____','_____','_____'],
    ['_____','_____','_____','_____','_____'],
    ['_____','_____','_____','_____','_____']
]


dungeon = [[], [], []]
dungeon[0]=[['start'], ['oldDagger'], ['zombie'], ['oldDagger'], ['suspiciousPotion']]
dungeon[1]=[['strongDagger'], ['zombie'],  ['oldDagger'],  ['nothing'], ['werewolf']],
dungeon[2]=[['zombie'], ['nothing'], ['zombie'], ['zombie'], ['silverKnife']],
    
roomContents = dungeon[plyrFloor] [plyrLocation]
dungeonLayout[plyrFloor][plyrRoom] =  '__x__'
gameRunning=True

while gameRunning:

    print(dungeonLayout[0])

    print(dungeonLayout[1])

    print(dungeonLayout[2])





    print('Your inventory' + str(plyrInventory))

    if 'oldDagger' in roomContents:
        print('There is an old dagger')
    if 'zombie' in roomContents:
        print('Inside the room is a zombie')
    if 'suspiciousPotion' in roomContents:
        print('On a table there sits a suspicious potion')
    if 'strongDagger' in roomContents:
        print('There is a nice dagger')
    if 'werewolf' in roomContents:
        print('A werewolf?!?!')
    if 'nothing' in roomContents:
        print('There is nothing in this room')
    if 'silverKnife' in roomContents:
        print('This knife looks different...')

    playerMove = input('What would you like to do?')


    if playerMove == 'h':
        print('l: go to the room on the left')
        print('r: go to the room on the right')
        print('up: go to the next floor')
        print('dwn: go to the previous floor')
        print('a: attack')
        print('g: grab an item')
        print('use: use an item')

            #move left
            #check if they can move left (is there a room on the left? is there a monster stopping them?)
            #update the player map (reset the current room before adding the x to the next) example:


    plyrRoom -= 1

    

    if playerMove == 'r':
        if plyrLocation < 4:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrLocation += 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'

    elif playerMove == 'l':
        if plyrLocation > 0:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrLocation -= 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'

    elif playerMove == 'u':
        if plyrLocation== 4:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrFloor += 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'
        
        if plyrLocation == 0:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrFloor += 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'

    elif playerMove == 'd':
        if plyrLocation == 4:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrFloor -= 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'
        if plyrLocation == 0:
            dungeonLayout[plyrFloor][plyrLocation] = '_____'
            plyrFloor -= 1
            dungeonLayout[plyrFloor][plyrLocation] = '__x__'

            if playerMove == 'f':
                if 'zombie' in roomContents:
                    plyrInventory.remove('oldDagger')
                    dungeon[0][2].remove('zombie')
                    print('The zombie is slain')
                elif 'werewolf' in roomContents:
                    plyrInventory.remove('silverKnife')
                    dungeon[0][2].remove('werewolf')
                    print('The werewolf is slain')

            if playerMove =='use':
                plyrInventory.remove('suspiciousPotion')
                print('Your stomach hurts as your skin begins to turn green')
                gameRunning = False

    if playerMove == 'g':
                if 'oldDagger' in roomContents:
                    plyrInventory.append('oldDagger')
                    dungeon[0][1].remove('oldDagger')
                elif 'strongDagger'in roomContents:
                    plyrInventory.append('strongDagger')
                    dungeon[1][3].remove('oldDagger')
                elif 'silverKnife'in roomContents:
                    plyrInventory.append('silverKnife')
                    dungeon[0][3].remove('oldDagger')
                elif 'suspiciousPotion'in roomContents:
                    plyrInventory.append('suspiciousPotion')
                    dungeon[2][2].remove('oldDagger')
                
                    time.sleep(1)