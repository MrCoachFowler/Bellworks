public class Test {
    
    private static int totalScore;
    private static int totalPointsPossible;
    private static int nextID;

    private int id;
    private int score;
    private int pointsPossible;

    public Test(int score, int pointsPossible)
    {
        this.id = nextID++;
        this.totalPointsPossible += pointsPossible;
        this.totalScore += score;
        this.score = score;
        this.pointsPossible = pointsPossible;
    }

    public static double getTotalAverage()
    {
        if (totalPointsPossible > 0)
        {
            return (double) totalScore / totalPointsPossible;
        }
        return 0;
    }

    public double getPercentage()
    {
        return (double) this.score / this.pointsPossible;
    }
}
