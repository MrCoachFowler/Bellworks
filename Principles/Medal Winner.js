function getRandomInteger(min, max)
{
    let range = max - min;
    let rand = Math.floor(Math.random() * range);
    return min + rand;
}

//Create a function following this contract:
//Name: awardMedals
//Purpose: takes a number between 1 and 8. If first place, say gold medal! If second or third, say made podium! Otherwise say not this time...
//Input: number between 1 and 8
//Output: String depeding on input number
function awardMedals(place)
{
    if (place <= 3)
    {
        if (place == 1)
        {
            return "Gold!!";
        }
        else
        {
            return "Podium!";
        }
    }
    else
    {
        return "Not this time...";
    }
}



//Create a program that:
//creates a random number between 1 and 8
//prints the result of the awardMedals function with the number created
let placing = getRandomInteger(1,8)
console.log(awardMedals(placing))