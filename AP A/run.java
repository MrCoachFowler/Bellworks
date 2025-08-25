
public class run 
{
    public static void main(String[] args) 
    {

        System.out.println(Test.getTotalAverage());
        
        Test t1 = new Test(80, 100);
        Test t2 = new Test(9, 10);

        System.out.println(t1.getPercentage());
        System.out.println(t2.getPercentage());
        System.out.println(Test.getTotalAverage());
    }
}
