
public class run 
{
    public static void main(String[] args) 
    {
        String[][] tester = {
            {"Hello", "Brave", "New", "World"},
            {"Skibidi", "Rizz", "Locked in", "Yeet"},
            {"I", "Love", "Computer Science", "The Most"},
            {"Christine", "Lucas", "Will", "Lucas"}
        };
        Helper.boxPrintColMajor(tester);


        System.out.println(litPart);
        System.out.println(lit);

        Musician m = new Musician("Guitar");
        
    }

    public static void print2DArray(Object[][] arr)
    {
        for(Object[] row : arr)
        {
            System.out.println("------------------------------");
            for(Object val : row)
            {
                System.out.print(" | " + val);
            }
            System.out.println(" |");
        }
        System.out.println("------------------------------");
    }

    
}
