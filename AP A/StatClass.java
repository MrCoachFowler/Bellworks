public class StatClass {
    //Make attributes to store the following information:
    //

    
    //make a constructor
    StatClass()
    {
        //nothing needed
    }

    //Make a method following the contract
    //Name: findAverage
    //Purpose: find the average of an array of values
    //Input: array of floats
    //Output: average of floats
    public double findAverage(double[] values)
    {
        double sum = 0;
        for(double value : values)
        {
            sum += value;
        }
        return sum / values.length;
    }

    //write a run file that:
    //finds the average of {10.2, 5, 43.23, 17.3, 23.90, 53.432}
}
