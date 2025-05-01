//Create a function following this contract:
//Name: rowColWinner
//Purpose: print which row has the highest average and which column has the highest average of any sized array
//Input: array to analyzie (arr)
//Output: None (prints index of highest average row and highest average column)
//your function code here...


//Create a program that:
//Uses the rowColWinner to analyze the randomly made array
let rowCount = 1 + Math.floor(Math.random() * 10) //generates a random number between 1 and 10
let colCount = 1 + Math.floor(Math.random() * 10) //generates a random number between 1 and 10
let arr = []

for(let i = 0; i < rowCount; i++)
{
    let row = [] //create an empty row
    for(let j = 0; j < colCount; j++)
    {
        row.push(Math.floor(Math.random() * 10)) //adds a random number between 0 and 9 to the row
    }
    arr.push(row)
}
console.log(arr)

//your code here...
