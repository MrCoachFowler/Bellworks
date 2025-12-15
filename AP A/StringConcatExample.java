public class StringConcatExample {
    public static void main(String args[])
    {
        String sLiteral = "Example";
        String sLiteral2 = "Concat";
        String sObject = new String(sLiteral);
        String sObject2 = new String("Concat");

        String combo = sLiteral + sLiteral2;
        sLiteral += sLiteral2;

        System.out.println(combo);
        System.out.println(sLiteral);
    }
}
