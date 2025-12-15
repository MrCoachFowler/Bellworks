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

#write a program that:
#prints hello world in green
greenPrint("Hello world")