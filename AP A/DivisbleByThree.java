public class DivisbleByThree {

    
    //make a main function that:
    //generates a random integer between 50 and 100, inclusive
    //prints the random generated number
    //prints whether the number is divisble by 3

    public static void main(String[] args)
    {
        int randNum = (int) (Math.random() * 51) + 50;
        System.out.println("Number: " + randNum);

        int charSum = 0;
        while(randNum > 0)
        {
            charSum += randNum % 10;
            randNum /= 10;
        }
        if (charSum % 3 == 0)
        {
            System.out.println("It is divisible by 3!");
        }
        else
        {
            System.out.println("It is not divisible by 3");
        }
    }
}
