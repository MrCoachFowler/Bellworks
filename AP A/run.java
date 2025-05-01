
public class run 
{
    public static void main(String[] args) 
    {
        String lit = "ABCDEFG";
        String litPart = lit.substring(4);
        lit = lit.substring(0, 3);

        System.out.println(litPart);
        System.out.println(lit);

        Musician m = new Musician("Guitar");
        
    }
}
