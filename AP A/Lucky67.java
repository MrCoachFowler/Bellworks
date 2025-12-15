public class Lucky67 {
    //Create a main method that...
    //Starts with the number 1
    //If the number is below 67, it adds a random number between itself and 67
    //If the number is above 67, it substracts a random number between half of itself and itself
    //Counts the number of times the number is changed
    //Once the number is 67, it prints how many times it was changed

    public static void main(String[] args)
    {
        int num = 1;
        int timesTried = 0;
        while(num != 67)
        {
            if(num < 67)
            {
                int randNumRange = 67 - num;
                num += (int) (Math.random() * randNumRange + 1) + num;
            }
            else
            {
                int randNumRange = num - num / 2;
                num -= (int) (Math.random() * randNumRange + 1) + num / 2;
            }
            timesTried++;
        }

        System.out.println("num is now: " + num);
        System.out.println("Times tried: " + timesTried);
    }
}
