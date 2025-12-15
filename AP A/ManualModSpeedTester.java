


public class run 
{
    public static void main(String[] args) 
    {

        long TEST_VAL = 1000000000L;

        System.out.println("Test Number is: " + TEST_VAL);

        long startTime = System.nanoTime();
        long testVal = TEST_VAL;
        while (testVal > 0)
        {
            testVal -= 3;
        }
        if(testVal == 0)
        {
            System.out.println("testVal divisible by 3: subtract3");
        }
        else
        {
            System.out.println("testVal is not divisble by 3: subtract 3");
        }
        long endTime = System.nanoTime();
        long elapsedTimeNanos = endTime - startTime;
        System.out.println("Took: " + elapsedTimeNanos + " nanoseconds");

        
        long startTime2 = System.nanoTime();
        long testVal2 = TEST_VAL;
        int sum = 0;
        while (testVal2 != 0)
        {
            sum += testVal2 % 10;
            testVal2 /= 10;
        }
        while(sum > 0)
        {
            sum -= 3;
        }
        if(sum == 0)
        {
            System.out.println("testVal divisible by 3: add and subtract3");
        }
        else
        {
            System.out.println("testVal is not divisble by 3: add and subtract 3");
        }
        long endTime2 = System.nanoTime();
        long elapsedTimeNanos2 = endTime2 - startTime2;
        System.out.println("Took: " + elapsedTimeNanos2 + " nanoseconds");


        long startTime3 = System.nanoTime();
        if (TEST_VAL % 3 == 0)
        {
            System.out.println("TestVal is divisble by 3: mod3");
        }
        else
        {
            System.out.println("testVal is not divisible by 3: mod3");
        }
        long endTime3 = System.nanoTime();
        long elapsedTimeNanos3 = endTime3 - startTime3;
        System.out.println("Took: " + elapsedTimeNanos3 + " nanoseconds");

        long startTime4 = System.nanoTime();
        long testVal4 = TEST_VAL;
        long flooredThird = testVal4 / 3L;
        testVal4 -= flooredThird * 3L;

        if(testVal4 == 0)
        {
            System.out.println("testVal divisible by 3: divide multiply3");
        }
        else
        {
            System.out.println("testVal is not divisble by 3: divide multiply 3");
        }
        long endTime4 = System.nanoTime();
        long elapsedTimeNanos4 = endTime4 - startTime4;
        System.out.println("Took: " + elapsedTimeNanos4 + " nanoseconds");

        




    }
}
