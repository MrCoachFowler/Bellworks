#name: wordFrequency
#purpose: create a dictionary that keeps track of what words were in a string and how often they were used
#input: a string containing words
#output: a dictionary with keys of words and value of how many times they appear in the string
def wordFrequency(paragraph):
    #remove all punctuation (add to list if needed)
    punctuations = [",", ".", "!", "?", ";", ":", "'", '"', "%", "$", "#", "@", "^", "&", "*", "(", ")" ,"\n"]
    for punctuation in punctuations:
        paragraph = paragraph.replace(punctuation, "")

    #force all letters to lowercase
    paragraph = paragraph.lower()

    #split the paragraph into a list of words
    wordList = paragraph.split(" ")

    #print(wordList)
    return wordList

    

testString = """Rainbow Road stands out as the quintessential Mario Kart track, capturing the essence of the franchise with its vibrant colors and challenging design. From the moment players race onto its luminescent surface, they are greeted by a breathtaking spectacle of swirling hues and celestial backdrops. This visually stunning track creates an immersive experience that transports players to a fantastical world, making each race feel like a grand adventure in space. The iconic music that accompanies the course enhances the excitement, evoking nostalgia for long-time fans while captivating newcomers.

What truly sets Rainbow Road apart is its notorious difficulty. The lack of barriers on many sections means that even the slightest miscalculation can lead to a spectacular fall into the void, heightening the stakes for every racer. This blend of challenge and thrill pushes players to refine their skills, mastering drifting and item usage to navigate the twists and turns effectively. The track’s layout, with its sharp corners and sudden drops, demands precision and strategy, turning each race into a test of both skill and resilience. The thrill of racing on Rainbow Road fosters a sense of camaraderie and rivalry, as players share the highs of their victories and the lows of their missteps.

Furthermore, Rainbow Road has become a symbol of the Mario Kart series, representing both nostalgia and a benchmark for future tracks. Its enduring presence across multiple installments of the game showcases its popularity and the affection fans have for it. Each iteration introduces new elements and challenges while retaining the core essence that makes Rainbow Road beloved. Whether racing against friends in multiplayer or going solo in time trials, players are drawn to the allure of this iconic track, making it a definitive favorite in the Mario Kart universe."""

#Feel free to print wordsToCount to see the word list
wordsToCount = wordFrequency(testString)
#todo: count the frequency of each word into a dictionary