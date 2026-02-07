public class run 
{
    public static Example test1(Example ex)
    {
        ex.updateVal();
        return ex;
    }

    public static void main(String[] args) 
    {
        int a = 1;
        boolean b = true;
        double x = 2.5;
        String s = "Hello";

        String ex1 = s + a;
        String ex2 = s + b;
        String ex3 = s + x;

        String ex4 = a + 5 + s + x + 1.5;

        System.out.println(ex1);
        System.out.println(ex2);
        System.out.println(ex3);
        System.out.println(ex4);
        
        
    }
}
