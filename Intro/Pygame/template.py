import pygame
from Screen import Screen

class Window:

    def __init__(self, title="Test App", colorRGB=False):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption(title)
        self.color = (0, 0, 0)
        if colorRGB:
            self.color = colorRGB
        self.screen.fill(self.color)

    def setColor(self, colorRGB):
        self.screen.fill(colorRGB)

  
    def update(self, screenObj=False):
        if screenObj:
            self.screen.fill(screenObj.color)
            screenObj.display()

        else:
            self.screen.fill(self.color)
        pygame.display.flip()

    def checkForInput(self):
        #check for inputs
        for event in pygame.event.get():
            print(event)
            #handle various inputs
            ##quit type    
            if event.type == pygame.QUIT: 
                pygame.quit()

