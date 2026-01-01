
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class WordScramble
{
    private int GRID_SIZE = 20;
    private ArrayList<ArrayList<String>> board = new ArrayList<>();
    private ArrayList<String> words = new ArrayList<>();

    public WordScramble(String wordFilePath)
    {
        this.loadWords(wordFilePath);
        this.loadEmptyBoard();
        this.placeWords();
        this.fillRemainingBoard();
    }

    private void loadWords(String wordFilePath)
    {
        File wordFile = new File(wordFilePath);
        try 
        {
            Scanner s = new Scanner(wordFile);

            while(s.hasNextLine())
            {
                String line = s.nextLine();
                String[] newValues  = line.split(",");
                for(String newValue : newValues)
                {
                    this.words.add(newValue);
                }
            }
        } catch (FileNotFoundException e) 
        {
            System.out.println("file not found by scanner");
        }
    }

    private void loadEmptyBoard()
    {
        for(int i = 0; i < this.GRID_SIZE; i++)
        {
            ArrayList<String> newRow = new ArrayList<>();
            for(int j = 0; j < this.GRID_SIZE; j++)
            {
                newRow.add("");
            }
            this.board.add(newRow);
        }
    }
    private void placeWords()
    {
        int[][] directions = new int[][] {
            {1, 0},
            {1, 1},
            {1, -1},
            {0, 1},
            {0, -1},
            {-1, 0},
            {-1, 1},
            {-1, -1}
        };
        for(String word : this.words) 
        {
            int randDirectionIndex = (int) (Math.random() * directions.length);
            int[] direction = directions[randDirectionIndex];
            boolean placed = false;
            while(!placed)
            {
                int maxX = Math.min(this.GRID_SIZE - word.length() * direction[0], this.GRID_SIZE);
                int minX = Math.max(0, -word.length() * direction[0]);

                int maxY = Math.min(this.GRID_SIZE - word.length() * direction[1], this.GRID_SIZE);
                int minY = Math.max(0, -word.length() * direction[1]);

                int randX = (int) (Math.random() * (maxX - minX)) + minX;
                int randY = (int) (Math.random() * (maxY - minY)) + minY;

                if (checkPlacement(randX, randY, word, direction))
                {
                    placeWord(randX, randY, word, direction);
                    placed = true;
                }

            }
        }
    }

    private boolean checkPlacement(int x, int y, String word, int[] direction)
    {
        for(int i = 0; i < word.length(); i++)
        {
            String boardSpot = this.board.get(x).get(y);
            if (!boardSpot.equals(""))
            {
                return false;
            }
            x += direction[0];
            y += direction[1];
        }
        return true;
    }

    private void placeWord(int x, int y, String word, int[] direction)
    {
        for(int i = 0; i < word.length(); i++)
        {
            String letter = word.substring(i, i+1);
            this.board.get(x).set(y, "\u001B[32m" + letter + "\u001B[0m");
            x += direction[0];
            y += direction[1];
        }
    }

    private void fillRemainingBoard()
    {
        String[] letters = new String[] {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        for(int i = 0; i < this.GRID_SIZE; i++)
        {
            for(int j = 0; j < this.GRID_SIZE; j++)
            {
                if(this.board.get(i).get(j).equals(""))
                {
                    int randIndex = (int) (Math.random() * letters.length);
                    String newLetter = letters[randIndex];
                    this.board.get(i).set(j, newLetter);
                }
            }
        }
    }
    public void print()
    {
        for(ArrayList<String> row : board)
        {
            System.out.print(" ");
            for(String letter : row)
            {
                System.out.print(letter + " ");
            }
            System.out.println();
        }
    }
}