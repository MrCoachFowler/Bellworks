import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Player {
    
    private String name;
    private ArrayList<Die> rollingDice = new ArrayList<>();
    private ArrayList<Die> heldDice = new ArrayList<>();
    private Scoreboard scoreboard = new Scoreboard();
    private Boolean isDone;
    
    public Player(String name)
    {
        this.name = name;
        this.isDone = false;
    }

    public void prepDice()
    {
        this.heldDice = new ArrayList<>();
        this.rollingDice = new ArrayList<>();

        for(int i = 0; i < 5; i++)
        {
            rollingDice.add(new Die());
        }
    }

    public String getName()
    {
        return this.name;
    }

    public void roll()
    {
        for(Die die : rollingDice)
        {
            die.roll();
        }
    }

    public void keepDice(Scanner scanner)
    {
        System.out.println("What are the position numbers of the dice you want to keep?");
        String keepString = scanner.nextLine();

        ArrayList<Integer> keepIndices = new ArrayList<>(); //the indices of the dice to be removed
        ArrayList<String> validKeeps = new ArrayList<>(); //list of valid indices the user can put
        for(int i = 0; i < this.rollingDice.size(); i++)
        {
            validKeeps.add(String.valueOf(i + 1));
        }

        //go through each letter in the string and find the valid indices
        for(int i = 0; i < keepString.length(); i++)
        {
            String keepValue = keepString.substring(i, i+1);
            if( validKeeps.contains(keepValue))
            {
                keepIndices.add(Integer.valueOf(keepValue) - 1); //safe to assume the values can be converted
            }
        }

        //reverse the order of the indices to not worry about index changes while removing
        Collections.sort(keepIndices, Collections.reverseOrder());

        //move the dice
        for(int keepIndex : keepIndices)
        {
            Die movingDie = this.rollingDice.remove(keepIndex);
            this.heldDice.add(movingDie);
        }
    }

    public void holdAllDice()
    {
        while(this.rollingDice.size() > 0)
        {
            this.heldDice.add(this.rollingDice.remove(0));
        }
    }
    public Boolean hasDiceLeft()
    {
        return this.rollingDice.size() > 0;
    }

    public void printDiceInRoll()
    {
        System.out.println("Dice still rollable: ");
        DiePrinter.print(this.rollingDice);

        System.out.println("Dice held:");
        DiePrinter.print(this.heldDice);
    }

    public void printDiceFinal()
    {
        System.out.println("Your final roll:");
        DiePrinter.print(this.heldDice);
    }

    public void printScoreboard()
    {
        this.scoreboard.print();
    }

    public void updateScore(Scanner scanner)
    {
        ArrayList<String> headings = new ArrayList<>(Arrays.asList("aces", "twos", "threes", "fours", "fives", "sixes", "three of a kind", "four of a kind", "full house", "small straight", "large straight", "chance", "yahtzee")); //list of valid responses
        System.out.println("Please type exactly which category you want to update:");
        String userChoice;

        while(true)
        {
            userChoice = scanner.nextLine().toLowerCase();
            if(headings.contains(userChoice)) {break;}
            else{ System.out.println("Hmm.. it wasn't recognized. Let's try again! What category do you want to update?");}
        }

        if(userChoice.equals("aces")) {this.scoreboard.setAces(this.heldDice);}
        else if(userChoice.equals("twos")) {this.scoreboard.setTwos(this.heldDice);}
        else if(userChoice.equals("threes")) {this.scoreboard.setThrees(this.heldDice);}
        else if(userChoice.equals("fours")) {this.scoreboard.setFours(this.heldDice);}
        else if(userChoice.equals("fives")) {this.scoreboard.setFives(this.heldDice);}
        else if(userChoice.equals("sixes")) {this.scoreboard.setSixes(this.heldDice);}

        else if(userChoice.equals("three of a kind")) {this.scoreboard.setThreeOfAKind(this.heldDice);}
        else if(userChoice.equals("four of a kind")) {this.scoreboard.setFourOfAKind(this.heldDice);}
        else if(userChoice.equals("full house")) {this.scoreboard.setFullHouse(this.heldDice);}
        else if(userChoice.equals("small straight")) {this.scoreboard.setSmallStraight(this.heldDice);}
        else if(userChoice.equals("large straight")) {this.scoreboard.setLargeStraight(this.heldDice);}
        else if(userChoice.equals("yahtzee")) {this.scoreboard.setYahtzee(this.heldDice);}
        else if(userChoice.equals("chance")) {this.scoreboard.setChance(this.heldDice);}


        

    }
}
