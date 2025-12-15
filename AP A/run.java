public class run 
{
    public static Example test1(Example ex)
    {
        ex.updateVal();
        return ex;
    }

    public static void main(String[] args) 
    {
        Example e = new Example();
        Example e2 = test1(e);

        System.out.println(e);
        System.out.println(e2);
    }
}