from template import Window


window = Window('Test Game')

gameOn = True
while gameOn:
    #do stuff here

    window.checkForInput()
    window.update()