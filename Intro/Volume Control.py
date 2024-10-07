#Make a function based on the following contract:
#Name: volumeControl
#Purpose: looks through a list of words and make uppercase if 'loud' or lowercase if 'quiet'
#Input: list of words
#Output: list of volume controlled words
def volumeControl(listOfWords):
    wordCounter = 0
    while wordCounter < len(listOfWords):
        word = listOfWords[wordCounter]
        if word == 'Quiet':
            listOfWords[wordCounter] = word.lower()
        elif listOfWords[wordCounter] == 'Loud':
            listOfWords[wordCounter] = word.upper()
        wordCounter += 1

    return listOfWords

#write a program that:
#takes in the following list and prints out a version where 'loud' is capitalized and 'quit' is lowercase
#['Medium', 'Mid', 'Lower-mid', 'Quiet', 'Quit', 'Not quiet', 'Loud', 'Screaming']
wordList = ['Medium', 'Mid', 'Lower-mid', 'Quiet', 'Quit', 'Not quiet', 'Loud', 'Screaming']
answer = volumeControl(wordList)
print(answer)