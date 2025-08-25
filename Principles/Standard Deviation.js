function randNumBetween(min, max)
{
    let range = max - min + 1
    return Math.floor(Math.random() * range + min)
}

//Create a function following this contract:
//Name: avg
//Purpose: Find the average of a list of numbers
//Input: a array of numbers
//Output: the average of those numbers
function avg(numList)
{
    let sum = 0
    for(let i = 0; i < numList.length; i++)
    {
        sum += numList[i]
    }
    return sum / numList.length
}

//Create a function following this contract:
//Name: stdev
//Purpose: Find the standard deviation of a list of numbers
//Input: a array of numbers
//Output: the standard deviation of those numbers
function stdev(numList)
{
    let sum = 0
    let mean = avg(numList)
    for(let i = 0; i < numList.length; i++)
    {
        let adder = (mean - numList[i]) ** 2
        sum += Math.sqrt(adder)
    }
    return sum / numList.length
}

//Create a program that:
//Creates a list of 1000 random numbers between 1 and 50
//Calculate and print the average of those numbers
//Calculate and print the standard deviation of those numbers
numsToGenerate = 1000
minNum = 1
maxNum = 50

let numList = []
for(let i = 0; i < numsToGenerate; i++)
{
    numList.push(randNumBetween(minNum, maxNum))
}

let mean = avg(numList)
let standardDeviation = stdev(numList)

console.log(numList)
console.log(mean)
console.log(standardDeviation)



//Once done, answer the following questions:
//1. How might you change how you generated your list to get an average close to 40?
//2. How might you change how you generated your list to reduce the standard deviation?