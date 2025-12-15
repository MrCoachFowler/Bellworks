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
function monteHall(switchOrNah)
{
    let doorsToRemove = [1, 2, 3]
    let doorsBeingShown = [1, 2, 3]

    let prizeDoor = randNumBetween(1, 3)

    //we can no longer remove that door
    doorsToRemove = doorsToRemove.filter(door => door != prizeDoor)
    
    let doorChosen = randNumBetween(1, 3)

    //we can no longer remove that door
    doorsToRemove = doorsToRemove.filter(door => door != doorChosen)

    //todo: remove one of the doors that can be removed
    //todo: remove that door from the doors being shown
    doorsBeingShown = doorsBeingShown.filter(door => door != doorsToRemove[0])

    //todo: if the player is switching, switch to the other door being shown, else stay at the first door chosen
    if(switchOrNah)
    {
        //take the door initially chosen out of the doors being shown. only door left is the door to switch to
        doorsBeingShown = doorsBeingShown.filter(door => door != doorChosen)
        doorChosen = doorsBeingShown[0]
    }
    //todo: return true if they win, false if they lose
    if (doorChosen == prizeDoor)
    {
        return true
    }
    else
    {
        return false
    }
}

//Create a program that:
//runs the monte hall problem 1000 times where the participant doesn't switch
//runs the monte hall problem 1000 times where the participant switches
//prints the percentage of wins from not switching
//prints the percentage of wins from switching
let trials = 1600000000
let wins = 0
for(let i = 0; i < trials; i++)
{
    if(monteHall(false))
    {
        wins++
    }
}
console.log("Without switching, the win rate was " + (wins / trials * 100) + " percent")

wins = 0
for(let i = 0; i < trials; i++)
{
    if(monteHall(true))
    {
        wins++
    }
}
console.log("With switching, the win rate was " + (wins / trials * 100) + " percent")