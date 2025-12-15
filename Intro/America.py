from colorama import Fore, Back

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
def addEmptyBlueSpacesToString(string, numSpaces):
    spaces = ""
    for i in range(numSpaces):
        spaces += " "
    return string + Back.BLUE + spaces + Back.RESET

#TODO: finish this function to make the desired american flag 
#stars are 5 rows of six with 4 rows of 5 between them
#Ours will have different spacing of stripes, but there must still be 13 stripes and some must be side by side with the stars
for i in range(13):
    string = ""
    #if in a star section...
    if i < 9:
        #use this to alternate the star position
        if i % 2 == 0:
            #one space before first star
            string = addEmptyBlueSpacesToString(string, 1)
            #add stars with equal spacing (doesn't include last star)
            for j in range(5):
                string = addWhiteStarWithBlueBackToString(string)
                string = addEmptyBlueSpacesToString(string, 3)
            #add last star with a space
            string = addWhiteStarWithBlueBackToString(string)
            string = addEmptyBlueSpacesToString(string, 1)

            #finish with red stripe
            for j in range(23):
                string = addRedSpaceToString(string)

        else:
            #this is the smaller, off centered star row
            #add three empty spaces to line it up
            string = addEmptyBlueSpacesToString(string, 3)
            #add a stars with equal spacing
            for j in range(5):
                string = addWhiteStarWithBlueBackToString(string)
                string = addEmptyBlueSpacesToString(string, 3)

            for j in range(23):
                string = addWhiteSpaceToString(string)

    #if not in star section
    elif i % 2 == 0:
        for j in range(46):
            string = addRedSpaceToString(string)
    else:
        for j in range(46):
            string = addWhiteSpaceToString(string)

    print(string)