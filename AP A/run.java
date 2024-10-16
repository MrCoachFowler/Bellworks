public class run {
    public static void main(String[] args) 
    {
        StatClass stat = new StatClass();
        double[] values = new double[]{10.2, 5, 43.23, 17.3, 23.90, 53.432};
        double avg = stat.findAverage(values);
        System.out.println(avg);
    }
    
}
