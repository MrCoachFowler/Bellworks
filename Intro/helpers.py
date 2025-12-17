from colorama import Fore

#Make a function based on the following contract:
#Name: greenPrint
#Purpose: print out green text and then set the color back
#Input: the string to be printed
#Output: void
def greenPrint(string):
    printStatement = Fore.GREEN
    printStatement += string
    printStatement += Fore.RESET
    print(printStatement)

#Make a function based on the following contract:
#Name: cPrint
#Purpose: print out text in a specific color
#Input: The text to be printed, the color to print as a string
#Output: void
def cPrint(text, color):
    colorList = [
        ['green', Fore.GREEN],
        ['red', Fore.RED],
        ['blue', Fore.BLUE],
        ['yellow', Fore.YELLOW],
        ['magenta', Fore.MAGENTA],
        ['cyan', Fore.CYAN]
    ]

    printStatement = ''
    #match color string to Fore value and add it to thing to be printed
    for c in colorList:
        if c[0] == color:
            printStatement += c[1]
            break
    printStatement += text

    printStatement += Fore.RESET

    print(printStatement)
    

#write a program that:
#prints hello world in green
greenPrint("Hello world")

#prints hello world in red
cPrint("Hello world", "red")

#Challenge: print Go Cats!!! where each character is on its own line and they alternate between red and blue
counter = 0
text = "Go Cats!!!"
for char in text:
    if counter % 2 == 0:
        cPrint(char, "red")
    else:
        cPrint(char, "blue")
    counter += 1