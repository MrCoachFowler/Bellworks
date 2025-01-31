class Screen:

    def __init__(self, window, colorRGB):
        self.surface = window.screen
        self.elements = []
        self.color = colorRGB

    def addPageElement(self, pageElement):
        self.elements.append(pageElement)

    def removePageElement(self, pageElement):
        self.elements.remove(pageElement)

    def display(self):
        for e in self.elements:
            e.display(self.surface)
        
        
