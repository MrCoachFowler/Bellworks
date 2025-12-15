from PyUI.Screen import Screen
from PyUI.PageElements import *

class FrameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0))
        self.word = "Hello"

    def elementsToDisplay(self):
        self.elements = [
            FlipperButton(self.word)
        ]

class FlipperButton(Button):
    def __init__(self, word):
        super().__init__((50, 50), 20, 20, word, (0,255,0))

    def onClick(self, screen):
        if screen.word == "Hello":
            screen.word = "World"
        else:
            screen.word = "Hello"