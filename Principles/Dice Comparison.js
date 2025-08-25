function randNumBetween(min, max)
{
    let range = max - min + 1
    return Math.floor(Math.random() * range + min)
}

//Create a function following this contract:
//Name: rollTwoSixDice
//Purpose: Generates two random values between 1 and 6 inclusive then returns their sum
//Input: void
//Output: int number representing the sum of the two random values generated
function rollTwoSixDice()
{
    let val1 = randNumBetween(1, 6)
    let val2 = randNumBetween(1, 6)
    return val1 + val2
}

//Create a function following this contract:
//Name: rollOneTwelveDie
//Purpose: Generates one random number between 1 and 12 inclusive then returns it
//Input: void
//Output: random int number between 1 and 12
function rollOneTwelveDie()
{
    return randNumBetween(1, 12)
}



//Create a program that:
//Rolls two six sided dice 1000 times and keeps track of results
//Rolls one twelve sided die 1000 times and keeps track of results
//Compares the average and standard deviation of the two different results
//Afterwards, describe if the results are the same or different and why this might be
let numRuns = 1000
let twoSixes = [0,0,0,0,0,0,0,0,0,0,0,0]
let oneTwelve = [0,0,0,0,0,0,0,0,0,0,0,0]

for(let i = 0; i < numRuns; i++)
{
    let res = rollTwoSixDice()
    twoSixes[res - 1]++

    res = rollOneTwelveDie()
    oneTwelve[res-1]++
}

let twoSixMean = Math.

console.log(twoSixes)
console.log(oneTwelve)