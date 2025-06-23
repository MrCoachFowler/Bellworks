from PyUI.Window import Window
##import the custom screens you made---
from InitScreen import InitScreen
from FrameScreen import FrameScreen
##-------------------------------------


window = Window("Example App", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
initScreen = InitScreen(window)
frameScreen = FrameScreen(window)
##-----------------------------------

screen = frameScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---



    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
