import java.util.ArrayList;

public class Die {
    //Make attributes to store the following information:
    //number of sides of the die
    //current value
    //number of times rolled
    public int sideNum;
    public int currVal;
    public int numTimesRolled;

    
    //make a default constructor setting number of sides to 6
    public Die()
    {
        this.sideNum = 6;
        this.currVal = 1;
        this.numTimesRolled = 0;
    }
    //make an overloaded constructor allowing specification of the number of sides of the die
    public Die(int faceVal)
    {
        this.sideNum = faceVal;
        this.currVal = 1;
        this.numTimesRolled = 0;
    }

    //Make a method to...
    //roll the dice
    public void roll()
    {
        this.currVal = (int) (Math.random() * this.sideNum) + 1;
        this.numTimesRolled++;
    }
    //get the dices value
    public int getValue()
    {
        return this.currVal;
    }
    //get the number of times rolled
    public int getTimesRolled()
    {
        return this.numTimesRolled;
    }

    //write a main method that....
    //simulates doing a yahtzee dice roll with one Die
    //simulates doing a yahtzee dice roll with an arraylist of Die Objects
    //simulates rolling a 20 sided die until it rolls a 20 then prints how many rolls it took

    public static void main(String[] args)
    {
        System.out.println("Yahtzee Single Dice");
        Die die = new Die();
        for(int i = 0; i < 6; i++)
        {
            die.roll();
            System.out.println(die.getValue());
        }

        System.out.println("Yahtzee ArrayList of Die");
        ArrayList<Die> dice = new ArrayList<>();
        for(int i = 0; i < 6; i++)
        {
            dice.add(new Die());
        }
        for(Die d : dice)
        {
            d.roll();
            System.out.println(d.getValue());
        }

        System.out.println("Twenty Sided Die Challenge:");
        Die twentySidedDie = new Die(20);
        while(twentySidedDie.getValue() != 20)
        {
            twentySidedDie.roll();
        }
        System.out.println("Value: " + twentySidedDie.getValue());
        System.out.println("Tries taken: " + twentySidedDie.getTimesRolled());
    }

}
