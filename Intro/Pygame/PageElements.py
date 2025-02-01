from pygame import Rect
import pygame

class PageElement:
    def __init__(self, topLeftLoc, width, height, colorRGB=(255,255,255)):
        self.rect = Rect(topLeftLoc[0], topLeftLoc[1], width, height)
        self.color = colorRGB

    def wasClicked(self, clickLoc):
        if self.rect.collidepoint(clickLoc[0], clickLoc[1]):
            return True
        return False
    
    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def onClick(self):
        print("You've clicked a useless page element")


class Button(PageElement):

    def __init__(self, topLeftLoc, width, height, textColorRGB=(0,0,0), backColorRGB=(255,255,255), text="Test"):
        super().__init__(topLeftLoc, width, height, backColorRGB)
        self.text = text
        font = pygame.font.Font('freesansbold.ttf', 14)
        self.textSurf = font.render(self.text, True, textColorRGB)
        #center the text in the box
        textRect = self.textSurf.get_rect()
        textRect.center = (self.rect[0] + width / 2, self.rect[1] + height / 2)
        self.textRect = textRect
    
    def onClick(self):
        print("a ha! You've found a useless button. Great Work")
        print('The text on this button is: ' + self.text)

    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.textSurf, self.textRect)

class Image(PageElement):
    def __init__(self, topLeftLoc, width, height, imagePath):
        super().__init__(topLeftLoc, width, height)
        self.imagePath = imagePath

    def display(self, surface):
        img = pygame.image.load(self.imagePath)
        surface.blit(img, (self.rect[0], self.rect[1]))


    def onClick(self):
        print("You've clicked a useless image")

class Label(PageElement):
    def __init__(self, topLeftLoc, width, height, text, fontSize=14, textColorRGB=(0,0,0)):
        super().__init__(topLeftLoc, width, height, None)
        self.text = text
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        self.textSurf = font.render(self.text, True, textColorRGB)
        #center the text in the box
        textRect = self.textSurf.get_rect()
        textRect.center = (self.rect[0] + width / 2, self.rect[1] + height / 2)
        self.textRect = textRect

    def display(self, surface):
        surface.blit(self.textSurf, self.textRect)

        
    