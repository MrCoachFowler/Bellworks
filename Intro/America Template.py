from colorama import Fore, Back

#Optional: update the red and white space functions to add a certain number of spaces based on a second argument
def addRedSpaceToString(string):
    return string + Back.RED + " " + Back.RESET

def addWhiteSpaceToString(string):
    return string + Back.WHITE + " " + Back.RESET

def addWhiteStarWithBlueBackToString(string):
    return string + Fore.WHITE + Back.BLUE + "*" + Fore.RESET + Back.RESET

#TODO: make the following function for use:
#name: addEmptyBlueSpacesToString
#purpose: takes in a string, adds a specified number of blue spaces, then gives it back
#input: string to add to and number of blue spaces to input
#ouput: the original string plus some blue spaces


#TODO: finish this program to make the desired american flag 
#stars are 5 rows of six with 4 rows of 5 between them
##rows that have 6 stars will have red stripes next to them, 5s will have white
#ours will have 9 stripes alongside the stars and 4 underneath alternating red and white starting with red
#the width of the stripe section will be equal to the star section on the top
string = ""
for i in range(5):
    string = addRedSpaceToString(string)
print(string)
string = ""
for j in range(5):
    string = addWhiteStarWithBlueBackToString(string)
print(string)
