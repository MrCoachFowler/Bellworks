//Create a function following this contract:
//Name: shapePrinter
//Purpose: prints out the shape specified in a 5x5 grid
//Input: shape to print (square or triangle)
//Output: void
function shapePrinter(shapeType)
{
    if(shapeType === "square")
    {
        let row = "- - - - -";
        for(let i = 0; i < 5; i++)
        {
            console.log(row);
        }
    }

    if(shapeType === "triangle")
    {
        for(let i = 0; i < 5; i++)
        {
            let row = "";
            for(let j = 0; j <= i; j++)
            {
                row += "- ";
            }
            console.log(row);
        }
    }
}


//Create a program that:
//prints a triangle
//prints a flat line to seperate shapes
//prints a rectangle
shapePrinter("square");
console.log();
console.log("------------------------------");
console.log();
shapePrinter("triangle");