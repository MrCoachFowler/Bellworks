public class Helper
{
    public static int longestWord(String[][] arr)
    {
        int longest = 0;
        for(int row = 0; row < arr.length; row++)
        {
            for(int col = 0; col < arr[0].length; col++)
            {
                if (arr[row][col].length() > longest) 
                {
                    longest = arr[row][col].length();
                }
            }
        }
        return longest;
    }

    public static String addSpaces(String val, int length)
    {
        String res = val;
        int bouncer = 0;
        int spacesToAdd = length - val.length();
        while(spacesToAdd > 0)
        {
            if(bouncer % 2 == 0)
            {
                res = " " + res;
            }
            else
            {
                res = res + " ";
            }
            spacesToAdd--;
            bouncer++;
        }
        return res;
    }
    public static void boxPrint(String[][] arr)
    {
        int maxWordLength = longestWord(arr);
        int topBorderLength = (maxWordLength + 2) * arr.length + arr.length + 1;
        String horizBorder = "";
        for(int i = 0; i < topBorderLength; i++)
        {
            horizBorder += "-";
        }
        
        for(String[] row : arr)
        {
            System.out.println(horizBorder);
            System.out.print("|");
            for(String val : row)
            {
                System.out.print(" " + addSpaces(val, maxWordLength) + " |");
            }
            System.out.println();
        }
        System.out.println(horizBorder);
    }

    public static void boxPrintColMajor(String[][] arr)
    {
        int maxWordLength = longestWord(arr);
        int topBorderLength = (maxWordLength + 2) * arr.length + arr.length + 1;
        String horizBorder = "";
        for(int i = 0; i < topBorderLength; i++)
        {
            horizBorder += "-";
        }
        
        for(int col = 0; col < arr[0].length; col++)
        {
            System.out.println(horizBorder);
            System.out.print("|");
            for(int row = 0; row < arr.length; row++)
            {
                System.out.print(" " + addSpaces(arr[row][col], maxWordLength) + " |");
            }
            System.out.println();
        }
        System.out.println(horizBorder);
    }
}