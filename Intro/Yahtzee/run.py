from GameParts import Player, Cup, Die

name = input('what is your name')
p1 = Player(name)

while True:
    p1.doTurn()