from PyUI.Screen import Screen
from PyUI.PageElements import *

class InitScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0))
        self.elements = [
            ButtonFlipper()
        ]


class ButtonFlipper(Button):
    def __init__(self):
        super().__init__((50, 50), 20, 20, "Hello", (0,255,0))

    def onClick(self, screen):
        if self.text == "Hello":
            self.text = "World"
        else:
            self.text = "Hello"