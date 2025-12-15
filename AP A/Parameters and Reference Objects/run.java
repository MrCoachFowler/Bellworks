public class run 
{
    public static ClassExample test1(ClassExample ex)
    {
        ex.updateVal();
        return ex;
    }

    public static void main(String[] args) 
    {
        ClassExample e = new ClassExample();
        ClassExample e2 = test1(e);
        e2.updateVal();

        System.out.println(e);
        System.out.println(e2);
    }

    // public static String britishize(String someString)
    // {
    //     someString = someString.substring(1);
    //     return someString;
    // }
    // public static void main(String[] args) 
    // {
    //     String hello = "hello";
    //     String otherString = britisize(hello);

    //     System.out.println(hello);
    //     System.out.println(otherString);
    // }

public static int maybeAdder(int someInt)
{
    someInt += 10;
    return someInt;
}
// public static void main(String[] args) 
// {
//     int someNum = 5;
//     int someOtherNum = maybeAdder(someNum);

//     System.out.println(someNum);
//     System.out.println(someOtherNum);
// }
}