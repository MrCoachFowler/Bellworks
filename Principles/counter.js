//Create a function following this contract:
//Name: counter
//Purpose: Counts to a specified number
//Input: Number to count to
//Output: void
function counter(number)
{
    loopCounter = 1
    while(loopCounter <= number)
    {
        console.log(loopCounter);
        loopCounter++;
    }
}


//Create a program that:
//Counts to 10
//Counts to 20
counter(10);
counter(20);