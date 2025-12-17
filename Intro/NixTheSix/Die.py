#Creates a class to make die objects from
#Each die object should have a value
#Each object should be able to roll itself
from random import randint
class Die:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = randint(1,6)