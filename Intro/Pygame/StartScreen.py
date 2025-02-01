from Screen import Screen
from PageElements import *

class startScreen(Screen):
    def __init__(self, window, colorRGB=(0,0,0)):
        super().__init__(window, colorRGB)
        self.state = "main"
        self.elements.append(Label((200, 200), 100, 100, self.state))



class startButton(Button):
    def __init__(self, topLeftLoc, width, height):
        super().__init__(topLeftLoc, width, height)
        