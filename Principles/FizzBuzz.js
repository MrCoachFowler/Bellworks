//Create a function following this contract:
//Name: fizzBuzz
//Purpose: count to a specified number
///if the number is divisible by three, print fizz instead
///if the number is divisible by 5, print buzz instead
///if the number is divisible by 3 and 5, print fizzbuzz instead
//Input: number to count to
//Output: void
function fizzBuzz(maxNum)
{
    for(let i = 1; i <= maxNum; i++)
    {
        if(i % 3 === 0 && i % 5 === 0)
        {
            console.log("FizzBuzz");
        }
        else if (i % 3 === 0)
        {
            console.log("Fizz");
        }
        else if (i % 5 === 0)
        {
            console.log("Buzz");
        }
        else
        {
            console.log(i);
        }
    }
}



//Create a program that:
//does fizzbuzz to 15
//does fizzbuzz to 30
//does fizzbuzz to 100
fizzBuzz(15);
fizzBuzz(30);
fizzBuzz(100);