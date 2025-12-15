public class run 
{
    public static Example test1(Example ex)
    {
        ex.updateVal();
        return ex;
    }

    public static void main(String[] args) 
    {
<<<<<<< HEAD
        System.out.println("Hello World");
        System.out.print("\033[H\033[2J");
=======
        Example e = new Example();
        Example e2 = test1(e);

        System.out.println(e);
        System.out.println(e2);
>>>>>>> e0a5c590761ea29fd67c4ac8c762aea63c42de47
    }
}