from Window import Window
from Screen import Screen
from PageElements import Button


window = Window('Test Game')

gameOn = True
while gameOn:
    #do stuff here
    menuScreen = Screen(window, (100, 100, 100))
    menuScreen.addPageElement(Button((50, 50), 100, 100, (200, 200, 200), "Hello"))


    
    window.checkForInput(menuScreen)
    window.update(menuScreen)