
import java.util.ArrayList;
import java.util.Scanner;

public class Run {
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in); //one scanner used all game, passed into methods
        ArrayList<Player> players = new ArrayList<>(); //make player list
        for(int i = 0; i < 1; i++)
        {
            System.out.println("What is player " + (i + 1) + "'s name?");
            String newName = scanner.nextLine();
            players.add(new Player(newName));
        }
        clearScreen();

        for(int i = 0; i < 13; i++)
        {
            for(Player player : players)
            {
                //player rolls their turn
                player.prepDice();
                int turnCounter = 0;
                while(turnCounter < 3 && player.hasDiceLeft())
                {
                    player.roll();
                    turnCounter++;

                    clearScreen();
                    System.out.println(player.getName() + "'s turn!");
                    player.printScoreboard();
                    player.printDiceInRoll();
                    player.keepDice(scanner);
                }
                player.holdAllDice(); //if there are unheld dice still..
                //player updates their scoreboard
                clearScreen();
                player.printScoreboard();
                player.printDiceFinal();
                player.updateScore(scanner);

                clearScreen();
                System.out.println(player.getName() + " your scoresheet is now: ");
                player.printScoreboard();
                System.out.println("Hit enter to continue...");
                scanner.nextLine();
            }
        }
    }

    public static void clearScreen()
    {
        System.out.print("\033[H\033[2J");
    }
}
