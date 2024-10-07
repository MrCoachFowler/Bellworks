import java.util.Arrays;
import java.util.Random;

public class BoxAndWhisker {
    //Make a method following the contract
    //Name: percentileFinder
    //Purpose: Identify the percentile of an array of ints
    //Input: set of integers, percentile
    //Output: the value at the defined percentile of the set of integers
    public static int percentileFinder(int[] nums, int percentile)
    {
        //use the length of the array and percentile to find at what index to look
        int numCount = nums.length;
        //use the int nature of the value to round value down
        int percentileValueIndex = numCount * percentile / 100;

        //sort the array then find the value at the index
        Arrays.sort(nums);
        return nums[percentileValueIndex];
    }

    //Make attributes to store the following information:
    //NA

    //write a main method that:
    public static void main(String[] args) 
    {
        //make random values
        int[] randomVals = new int[100];
        Random rnd = new Random();
        for(int i = 0; i < randomVals.length; i++)
        {
            randomVals[i] = rnd.nextInt(1, 200);
            System.out.print(randomVals[i] + ",");
        }
        System.out.println();
        
        //calculates the 50 percentile of a random set of 100 numbers between 1 and 200
        int fiftyPercentile = percentileFinder(randomVals, 50);
        System.out.println(fiftyPercentile);
        //calculates the 25 percentile of the same random set of numbers
        int twentyFifthPercentile = percentileFinder(randomVals, 25);
        System.out.println(twentyFifthPercentile);
        //calculates the 75 percentile of the same random set of numbers
        int seventyFifthPercentile = percentileFinder(randomVals, 75);
        System.out.println(seventyFifthPercentile);

    }
}
