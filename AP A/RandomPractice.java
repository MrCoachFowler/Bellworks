import static java.lang.Math.random;

public class RandomPractice
{
    public static int randSixDice()
    {
        int val = (int) (random() * 6) + 1;
        return val;
    }
}
