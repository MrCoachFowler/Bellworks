
public class Randomizer {
    public static int randDie()
    {
        int val = (int) (Math.random() * 6) + 1;
        return val;
    }

    public static int randTwelveDie()
    {
        int val = (int) (Math.random() * 12) + 1;
        return val;
    }
}
