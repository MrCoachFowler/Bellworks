public class ManualMod {
    public static void main(String[] args)
    {
        // Write a static method to compute the modulus of two numbers without using a modulus function or operator
        // Then use it to print the result of:
        //     254 % 12 (2)
        //     85304 % 17 (15)
        //     2084729384 % 23843 (16679)
        System.out.println(manMod1(254, 12));
        System.out.println(manMod2(254, 12));
        System.out.println(manMod1(85304, 17));
        System.out.println(manMod2(85304, 17));
        System.out.println(manMod1(2084729384, 23843));
        System.out.println(manMod2(2084729384, 23843));
    }

    public static int manMod1(int a, int b)
    {
        while(a >= b)
        {
            a = a - b;
        }
        return a;
    }

    public static int manMod2(int a, int b)
    {
        int multi = a / b;
        return a - b * multi;
    }
}
