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
function monteHall(triesSwitching)
{
    //keep track of doors that can be removed
    let doorsThatCanBeRemoved = [1, 2, 3]
    let doorsShownToParticipant = [1, 2, 3]

    //choose the winning door then remove it from doors that can be removed
    let winningDoor = randNumBetween(1,3);
    doorsThatCanBeRemoved = doorsThatCanBeRemoved.filter(num => num != winningDoor)

    //participant chooses random door then remove it from doors that can be removed
    let doorChosen = randNumBetween(1,3);
    doorsThatCanBeRemoved = doorsThatCanBeRemoved.filter(num => num != doorChosen);

    //remove a door that doesn't have the prize and wasn't chosen
    doorsShownToParticipant = doorsShownToParticipant.filter(num => num != doorsThatCanBeRemoved[0])

    if (triesSwitching)
    {
        doorChosen = doorsShownToParticipant.filter(num => num != doorChosen)[0]
    }
    if (doorChosen == winningDoor)
    {
        return true
    }
    return false
}


//Create a program that:
//runs the monte hall problem 1000 times where the participant doesn't switch
//runs the monte hall problem 1000 times where the participant switches
//prints the percentage of wins from not switching
//prints the percentage of wins from switching

//no switch
let attemptCount = 1000
let winCount = 0;
for(let i = 0; i < attemptCount; i++)
{
    if (monteHall(false)) {winCount++}
}
console.log("Without switching, the win percentage is: " + winCount/attemptCount*100 + "%");

//switch
winCount = 0;
for(let i = 0; i < attemptCount; i++)
{
    if (monteHall(true)) {winCount++}
}
console.log("With switching, the win percentage is: " + winCount/attemptCount*100 + "%");