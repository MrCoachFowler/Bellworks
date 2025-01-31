diff_Slang = {
    "cap": 'Short for "lying", call someone out for lying.',
    "fam": 'Short for family. However can be used to describe your friend, like using "bro."',
    "bet": 'term for affirmation or agreement',
    "lit": 'Used to describe something exciting, enjoyable, or cool.',
    "goat":'Greatest Of All Time.'"describe somebody, like how people say Messi or Ronaldo is the GOAT.",
    "slaps":'something really good or enjoyable.',
    "glow up": 'somebody who over a course of time improved on their looks.',
    "sus": "suspicous",
    "ghosted": " when somebody texts you and you dont reply. or the oppostie."
}

# print (diff_Slang)
while True:
    userInput = input('what word do you want help with?').lower()
    if userInput in diff_Slang:
        print (diff_Slang.get(userInput))
        #give them the explanation
    elif userInput == 'q':
        break
    else:
        print ("Sorry this ain't in the dictionary")