class Example:
    test1 = []

    def __init__(self, value):
        self.test1.append(1)

        self.test2 = []
        self.test2.append(1)

    def printInfo(self):
        print("test1: ", self.test1)
        print("test2: ", self.test2)


firstObj = Example(4)
secondObj = Example(5)

print("Obj1")
firstObj.printInfo()

print("#------------------------------------------#")
print("Obj2")
secondObj.printInfo()