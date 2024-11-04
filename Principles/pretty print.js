//Write a function based on the following contract:
//Name: prettyPrint
//Purpose: Print a string with color
//Input(s): The string to print and the color to use
//Output: void
function prettyPrint(text, color)
{
    let reset = "\x1b[0m";
    let green = "\x1b[32m";
    let white = "\x1b[37m";

    if(color === "green")
    {
        console.log(green + text + reset);
    }
    else if(color === "white")
    {
        console.log(white + text + reset);
    }
    else
    {
        console.log(text);
    }
}


//Write a program that:
//spells out "supercalifragilisticexpialidocious" but colors the vowels green and other letters white
//prints the list ["Go Hawks","Tanque Verde", "Hawk Pride", "Hawk yeah!"] alternating between white and green
let vowels = ["a", "e", "i", "o", "u"];
let textToPrint = "supercalifragilisticexpialidocious";

for(let i = 0; i < textToPrint.length; i++)
{
    let letter = textToPrint[i];
    
    if(vowels.includes(letter))
    {
        prettyPrint(letter, "green");
    }
    else
    {
        prettyPrint(letter, "white");
    }
};

let listToPrint = ["Go Hawks","Tanque Verde", "Hawk Pride", "Hawk yeah!"];
let bouncer = 1;
listToPrint.forEach((item) =>
{
    if(bouncer === 1)
    {
        prettyPrint(item, "white");
        bouncer = 0;
    }
    else
    {
        prettyPrint(item, "green");
        bouncer = 1;
    }
})



