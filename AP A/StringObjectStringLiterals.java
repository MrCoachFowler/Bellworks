public class StringObjectStringLiterals {
    public static void main(String[] args)
    {
        // String sOne = "abc";
        // String sTwo = "def";
        // String sThree = sOne + sTwo;
        // String sFour = sThree.substring(2, 5);

        // String sObjectOne = new String("abc");
        // String sObjectTwo = new String("def");
        // String sObjectThree = new String(sOne + sTwo);
        // String sObjectFour = sObjectThree.substring(2, 5);

        // String a = "ABCDEFGHI";
        // String b = a.substring(3);
        // a = a.substring(0,4);
        
        // System.out.print(a);
        // System.out.println(b);

        // int a = 1;
        // boolean b = true;
        // double x = 2.5;
        // String s = "Hello";

        // String ex1 = s + a;
        // String ex2 = s + b;
        // String ex3 = s + x;

        // String a = "Example";
        // String b = "Example";
        // System.out.println(a == b);

        // String c = new String("Example");
        // String d = new String("Example");
        // System.out.println(c == d);


        int a = 5;
        Integer b = new Integer(a); //boxing
        Integer c = a; //boxing

        System.out.println(b); //unboxing
        int d = b; //unboxing
    }
}
