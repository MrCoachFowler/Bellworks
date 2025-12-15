public class FindMinInArray {
    private static int[] testOne = new int[] {12, 50, 84, 100, 54, 42};
    private static int[] testTwo = new int[] {53, 35, 8, -1, 5, 1232};
    private static int[] testThree = new int[] {12, 5, 12, 10, 57, 4};

    //Create a method that:
    //name: findMin
    //parameter: one int array
    //return: void
    //purpose: Print the min value and its index in the array
    public static void findMin(int[] arr)
    {
        int minI = 0;
        int minV = arr[0];

        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] < minV)
            {
                minV = arr[i];
                minI = i;
            }
        }
        System.out.println("Min Value: " + minV + " Min Index: " + minI);
    }

    //create a main method that:
    //calls the findMin method on each of the test int arrays
    //it should print:
    //testOne: 12, 0
    //testTwo: -1, 3
    //testThree: 4, 5
    //However, it should work for any sized int array with any values
    public static void main(String[] args)
    {
        findMin(testOne);
        findMin(testTwo);
        findMin(testThree);
    }
}
