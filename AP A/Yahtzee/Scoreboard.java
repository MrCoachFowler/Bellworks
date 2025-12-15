import java.util.ArrayList;

public class Scoreboard {
    
    private int aces;
    private int twos;
    private int threes;
    private int fours;
    private int fives;
    private int sixes;
    private int bonus;

    private int threeOfAKind;
    private int fourOfAKind;
    private int fullHouse;
    private int smallStraight;
    private int largeStraight;
    private int yahtzee;
    private int chance;

    public Scoreboard()
    {
        this.aces           = -1;
        this.twos           = -1;
        this.threes         = -1;
        this.fours          = -1;
        this.fives          = -1;
        this.sixes          = -1;
        this.bonus          = 0;
        this.threeOfAKind   = -1;
        this.fourOfAKind    = -1;
        this.fullHouse      = -1;
        this.smallStraight  = -1;
        this.largeStraight  = -1;
        this.yahtzee        = -1;
        this.chance         = -1;
    }

    private int getDiceCountByValue(ArrayList<Die> dice, int targetVal)
    {
        int count = 0;
        for(Die die : dice)
        {
            if( die.getValue() == targetVal )
            {
                count++;
            }
        }
        return count;
    }

    private int getTopTotal()
    {
        int total = 0;

        total += Math.max(this.aces  , 0);
        total += Math.max(this.twos  , 0);
        total += Math.max(this.threes, 0);
        total += Math.max(this.fours , 0);
        total += Math.max(this.fives , 0);
        total += Math.max(this.sixes , 0);
        total += Math.max(this.bonus , 0);

        return total;
    }

    private int getBottomTotal()
    {
        int total = 0;

        total += Math.max(this.threeOfAKind     , 0);
        total += Math.max(this.fourOfAKind      , 0);
        total += Math.max(this.fullHouse        , 0);
        total += Math.max(this.smallStraight    , 0);
        total += Math.max(this.largeStraight    , 0);
        total += Math.max(this.yahtzee          , 0);

        return total;
    }

    private int getGrandTotal()
    {
        int total = this.getBottomTotal();
        total += this.getTopTotal();
        return total;
    }

    private int getDiceTotal(ArrayList<Die> dice)
    {
        int total = 0;
        for(Die die : dice)
        {
            total += die.getValue();
        }
        return total;
    }

    private void updateBonus()
    {
        if(this.bonus == 0 && this.getTopTotal() >= 63)
        {
            this.bonus = 35;
        }
    }

    public void setAces(ArrayList<Die> dice)
    {
        this.aces = this.getDiceCountByValue(dice, 1);
        this.updateBonus();
    }

    public void setTwos(ArrayList<Die> dice)
    {
        this.twos = 2 * this.getDiceCountByValue(dice, 2);
        this.updateBonus();
    }

    public void setThrees(ArrayList<Die> dice)
    {
        this.threes = 3 * this.getDiceCountByValue(dice, 3);
        this.updateBonus();
    }

    public void setFours(ArrayList<Die> dice)
    {
        this.fours = 4 * this.getDiceCountByValue(dice, 4);
        this.updateBonus();
    }

    public void setFives(ArrayList<Die> dice)
    {
        this.fives = 5 * this.getDiceCountByValue(dice, 5);
        this.updateBonus();
    }

    public void setSixes(ArrayList<Die> dice)
    {
        this.sixes = 6 * this.getDiceCountByValue(dice, 6);
        this.updateBonus();
    }

    public void setThreeOfAKind(ArrayList<Die> dice)
    {
        Boolean hasProperDice = false;
        //check each value and see if they have three of a kind
        for(int i = 1; i <= 6; i++)
        {
            if(this.getDiceCountByValue(dice, i) >= 3)
            {
                hasProperDice = true;
                break;
            }
        }
        //if they have a three of a kind, they get the toal of their dice otherwise 0
        if(hasProperDice) {this.threeOfAKind = this.getDiceTotal(dice);}
        else {this.threeOfAKind = 0;}
    }

    public void setFourOfAKind(ArrayList<Die> dice)
    {
        Boolean hasProperDice = false;
        //check each value and see if they have three of a kind
        for(int i = 1; i <= 6; i++)
        {
            if(this.getDiceCountByValue(dice, i) >= 4)
            {
                hasProperDice = true;
                break;
            }
        }
        //if they have a three of a kind, they get the toal of their dice otherwise 0
        if(hasProperDice) {this.fourOfAKind = this.getDiceTotal(dice);}
        else {this.fourOfAKind = 0;}
    }

    public void setFullHouse(ArrayList<Die> dice)
    {
        Boolean hasTwo = false;
        Boolean hasThree = false;
        for(int i = 1; i <= 6; i++)
        {
            if(this.getDiceCountByValue(dice, i) == 2) {hasTwo = true;}
            if(this.getDiceCountByValue(dice, i) == 3) {hasThree = true;}
        }

        if(hasTwo && hasThree) {this.fullHouse = 25;}
        else {this.fullHouse = 0;}
    }

    public void setSmallStraight(ArrayList<Die> dice)
    {
        //create a 2d array of all possible small straights
        int[][] possStraights = new int[][] {
            {1, 2, 3, 4},
            {2, 3, 4, 5},
            {3, 4, 5, 6}
        };

        Boolean hasStraight = false;
        //check to see if they have one of the possible combinations
        for(int[] straight : possStraights)
        {
            Boolean hasAll = true;
            //if they have at least one of each required value for this straight, then break and say they have it
            for(int val : straight) 
            {
                if(this.getDiceCountByValue(dice, val) == 0)
                {
                    hasAll = false;
                    break;
                }
            }
            if(hasAll)
            {
                hasStraight = true;
                break;
            }
        }

        if (hasStraight) {this.smallStraight = 30;}
        else {this.smallStraight = 0;}
    }

    public void setLargeStraight(ArrayList<Die> dice)
    {
        //create a 2d array of all possible small straights
        int[][] possStraights = new int[][] {
            {1, 2, 3, 4, 5},
            {2, 3, 4, 5, 6}
        };

        Boolean hasStraight = false;
        //check to see if they have one of the possible combinations
        for(int[] straight : possStraights)
        {
            Boolean hasAll = true;
            //if they have at least one of each required value for this straight, then break and say they have it
            for(int val : straight) 
            {
                if(this.getDiceCountByValue(dice, val) == 0)
                {
                    hasAll = false;
                    break;
                }
            }
            if(hasAll)
            {
                hasStraight = true;
                break;
            }
        }

        if (hasStraight) {this.largeStraight = 40;}
        else {this.largeStraight = 0;}
    }

    public void setYahtzee(ArrayList<Die> dice)
    {
        Boolean hasYahtzee = false;
        for(int diceVal = 1; diceVal <= 6; diceVal++)
        {
            if(this.getDiceCountByValue(dice, diceVal) == 5)
            {
                hasYahtzee = true;
                break;
            }
        }

        if(hasYahtzee)
        {
            if(this.yahtzee == -1) { this.yahtzee = 50;}
            else {this.yahtzee += 100;}
        }
        else {this.yahtzee = 0;}
    }

    public void setChance(ArrayList<Die> dice)
    {
        this.chance = this.getDiceTotal(dice);
    }

    //FROM AI: USED TO PRINT BLANK IF NOT DONE WITH THE PRINT FUNCTION ----------
    private String show(int value) 
    {
        return (value == -1) ? "" : String.valueOf(value);
    }

    public void print()
    {
        System.out.println("┌────────────────────────┬────────┐");
        System.out.println("│       YAHTZEE SCORE    │ SCORE  │");
        System.out.println("├────────────────────────┼────────┤");
        System.out.println("│ UPPER SECTION          │        │");
        System.out.println("├────────────────────────┼────────┤");
        System.out.println(String.format("│ %-22s │ %6s │", "Aces (1s)",   show(aces)));
        System.out.println(String.format("│ %-22s │ %6s │", "Twos (2s)",   show(twos)));
        System.out.println(String.format("│ %-22s │ %6s │", "Threes (3s)", show(threes)));
        System.out.println(String.format("│ %-22s │ %6s │", "Fours (4s)",  show(fours)));
        System.out.println(String.format("│ %-22s │ %6s │", "Fives (5s)",  show(fives)));
        System.out.println(String.format("│ %-22s │ %6s │", "Sixes (6s)",  show(sixes)));
        System.out.println("├────────────────────────┼────────┤");
        System.out.println(String.format("│ %-22s │ %6d │", "Bonus", this.bonus));
        System.out.println(String.format("│ %-22s │ %6d │", "Upper Total", this.getTopTotal()));
        System.out.println("├────────────────────────┼────────┤");

        System.out.println("│ LOWER SECTION          │        │");
        System.out.println("├────────────────────────┼────────┤");
        System.out.println(String.format("│ %-22s │ %6s │", "3 of a Kind",    show(threeOfAKind)));
        System.out.println(String.format("│ %-22s │ %6s │", "4 of a Kind",    show(fourOfAKind)));
        System.out.println(String.format("│ %-22s │ %6s │", "Full House",     show(fullHouse)));
        System.out.println(String.format("│ %-22s │ %6s │", "Small Straight", show(smallStraight)));
        System.out.println(String.format("│ %-22s │ %6s │", "Large Straight", show(largeStraight)));
        System.out.println(String.format("│ %-22s │ %6s │", "Yahtzee",        show(yahtzee)));
        System.out.println(String.format("│ %-22s │ %6s │", "Chance",         show(chance)));
        System.out.println("├────────────────────────┼────────┤");
        System.out.println(String.format("│ %-22s │ %6d │", "Lower Total", this.getBottomTotal()));
        System.out.println("├────────────────────────┼────────┤");
        System.out.println(String.format("│ %-22s │ %6d │", "GRAND TOTAL", this.getGrandTotal()));
        System.out.println("└────────────────────────┴────────┘");
    }
}
