function getRandomNum(min, max)
{
    let range = max - min
    return Math.floor(Math.random() * (range + 1) + min)
}

//Create a function following this contract:
//Name: makeMineField
//Purpose: Create an 8x8 array where there are 10 bombs placed at random
//Input: None
//Output: 8x8 array of zeros where ten random spots are 1s
function makeMineField()
{
    let mineField = []
    const SIZE = 8
    for(let i = 0; i < SIZE; i++)
    {
        let row = [];
        for(let j = 0; j < SIZE; j++)
        {
            row.push(0)
        }
        mineField.push(row)
    }
    console.log(mineField)

    let minesPlaced = 0
    while (minesPlaced < 10)
    {
        let randX = getRandomNum(0, SIZE - 1)
        let randY = getRandomNum(0, SIZE - 1)
        console.log(randX)
        if (mineField[randX][randY] == 0)
        {
            mineField[randX][randY] = 1
            minesPlaced += 1
        }
    }
    return mineField
}



//Create a program that:
//Create an 8x8 minefield
//prints the minefield to the console
let mineField = makeMineField()
console.log(mineField)