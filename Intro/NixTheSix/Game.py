#This is the run file
#It needs to:
##Create 4 player objects in a list
##For six turns, have each player play their turn
##After six turns, print the score in ranked order (1st, 2nd, 3rd, 4th)
from Player import Player
import os

PLAYER_COUNT = 4
ROUND_COUNT = 2
players = []
for i in range(PLAYER_COUNT):
    print('What is player', str(i + 1) + "'s name?")
    newName = input()
    players.append(Player(newName))


for i in range(ROUND_COUNT):
    os.system('cls')
    print("It's round " + str(i + 1) + "!!")
    print("The current scores are...")
    for player in players:
        print(player.name + ": " + str(player.score) + " points")
    input('Enter to start the next round...')

    for player in players:
        os.system('cls')
        player.playTurn()


os.system('cls')
print('Here are the final results!!!')
while(len(players) > 0):
    maxPlayer = players[0]
    for player in players:
        if player.score > maxPlayer.score:
            maxPlayer = player

    print('Player: ' + maxPlayer.name + ' had ' + str(maxPlayer.score) + ' points!')
    players.remove(maxPlayer)