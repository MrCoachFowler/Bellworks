
public class run {
    public static void main(String[] args) 
    {
        int numRounds = 4;
        int value = 5;

        for(int i = 0; i < numRounds; i++)
        {
            boolean gotValue = false;
            while(!gotValue)
            {
                int rndVal = (int) Math.random() * 10;
                System.out.print(rndVal);
                if(rndVal == value)
                {
                    gotValue = true;
                }
            }
            System.out.println();
        }
    }
    
}
