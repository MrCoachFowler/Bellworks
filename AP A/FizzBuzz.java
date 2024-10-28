public class FizzBuzz {
    //Make attributes to store the following information:
    //NA

    
    //make a constructor
    //NA

    //Make a method following the contract
    //Name: doThing
    //Purpose: Make and print a list of numbers between 1 and 100
    ///if a number is divisible by 3, print fizz instead
    ///if a number is divisible by 5, print buzz instead
    ///if a number is divisible by 3 and 5, print fizzbuzz
    //Input: void
    //Output: void

    public void dothing()
    {
        int counter = 1;
        while(counter < 100)
        {
            boolean isDivis = false;
            if(counter % 3 == 0)
            {
                System.out.print("Fizz");
                isDivis = true;
            }
            if(counter %5 == 0)
            {
                System.out.print("Buzz");
                isDivis = true;
            }
            if(!isDivis)
            {
                System.out.print(counter);
            }
            System.out.print(", ");
            counter ++;

        }
    }

    //write a test file that:
    //runs the fizzbuzz
}
