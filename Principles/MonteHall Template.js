function randNumBetween(min, max)
{
    let range = max - min + 1
    return Math.floor(Math.random() * range + min)
}

//Create a function following this contract:
//Name: monteHall
//Purpose: Simulate one game of a monte hall
//Input: boolean switch - determines if the person switches their bet
//Output: true if the participant won, false if they lost


//Create a program that:
//runs the monte hall problem 1000 times where the participant doesn't switch
//runs the monte hall problem 1000 times where the participant switches
//prints the percentage of wins from not switching
//prints the percentage of wins from switching
