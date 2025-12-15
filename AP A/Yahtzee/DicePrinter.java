import java.util.ArrayList;

public class DicePrinter {

    private ArrayList<String> oneDie = new ArrayList<>();
    private ArrayList<String> twoDie = new ArrayList<>();
    private ArrayList<String> threeDie = new ArrayList<>();
    private ArrayList<String> fourDie = new ArrayList<>();
    private ArrayList<String> fiveDie = new ArrayList<>();
    private ArrayList<String> sixDie = new ArrayList<>();
    private ArrayList<ArrayList<String>> dieFaces = new ArrayList<>();
    
    public DicePrinter()
    {
        this.oneDie.add("#########");
        this.oneDie.add("#       #");
        this.oneDie.add("#   o   #");
        this.oneDie.add("#       #");
        this.oneDie.add("#########");

        this.twoDie.add("#########");
        this.twoDie.add("# o     #");
        this.twoDie.add("#       #");
        this.twoDie.add("#     o #");
        this.twoDie.add("#########");

        this.threeDie.add("#########");
        this.threeDie.add("# o     #");
        this.threeDie.add("#   o   #");
        this.threeDie.add("#     o #");
        this.threeDie.add("#########");

        this.fourDie.add("#########");
        this.fourDie.add("# o   o #");
        this.fourDie.add("#       #");
        this.fourDie.add("# o   o #");
        this.fourDie.add("#########");

        this.fiveDie.add("#########");
        this.fiveDie.add("# o   o #");
        this.fiveDie.add("#   o   #");
        this.fiveDie.add("# o   o #");
        this.fiveDie.add("#########");

        this.sixDie.add("#########");
        this.sixDie.add("# o   o #");
        this.sixDie.add("# o   o #");
        this.sixDie.add("# o   o #");
        this.sixDie.add("#########");

        this.dieFaces.add(oneDie);
        this.dieFaces.add(twoDie);
        this.dieFaces.add(threeDie);
        this.dieFaces.add(fourDie);
        this.dieFaces.add(fiveDie);
        this.dieFaces.add(sixDie);
    }

    public void print(ArrayList<Die> dice)
    {
        int dieHeight = oneDie.size();
        int dieWidth = oneDie.get(0).length();
        String seperator = "  ";
        String posStarter = "";
        for(int i = 0; i < dieWidth/2; i++)
        {
            posStarter += " ";
        }
        String posEnder = "";
        for(int i = 1; i < dieWidth - dieWidth/2; i++)
        {
            posEnder += " ";
        }

        int place = 1;
        for(Die die : dice)
        {
            System.out.print(posStarter + place + posEnder + seperator);
            place += 1;
        }
        System.out.println();

        for(int i = 0; i < dieHeight; i++)
        {
            for(Die die : dice)
            {
                int dieIndex = die.getValue() - 1;
                String diePiece = dieFaces.get(dieIndex).get(i);
                System.out.print(diePiece + seperator);
            }
            System.out.println();
        }
    }

}