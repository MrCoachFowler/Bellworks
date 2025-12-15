import java.util.ArrayList;

public class RandomChallenge {
    //Write a main method that...
    //gets 3 different random letters from the first word of the testString
    //gets 2 random, sequential letters from the second word of the testString
    //switches two random letters in the last word of the testString
    //NOTE: your code must work even if the testString is changed to another four word phrase
    public static String testString = "Tanque Verde Code Hawks";

    public static void main(String[] args) {

        //get all the space locations for use later
        ArrayList<Integer> spaceIndices = new ArrayList<>();
        int nextSpaceIndex = testString.indexOf(" ");
        while (nextSpaceIndex > -1)
        {
            spaceIndices.add(nextSpaceIndex);
            nextSpaceIndex = testString.indexOf(" ", nextSpaceIndex + 1);
        }
        
        //word 1 challenge
        ////get random indices in length of word
        ArrayList<Integer> firstRandoms = new ArrayList<>();
        int wordEnd = spaceIndices.get(0);
        while(firstRandoms.size() < 3)
        {
            Integer randIndex = (int) (Math.random() * wordEnd);
            if(!firstRandoms.contains(randIndex)) //prevent duplicates
            {
                firstRandoms.add(randIndex);
            }
        }
        
        ////print out the letters at those indices
        System.out.println("Random letters from first word");
        for(Integer r : firstRandoms)
        {
            System.out.print(testString.substring(r, r + 1) + ", ");
        }
        System.out.println(); //add some space between prints

        //word 2 challenge
        ////get proper word
        int wordStart = spaceIndices.get(0) + 1; //word after the first space
        wordEnd = spaceIndices.get(1);
        String secondWord = testString.substring(wordStart, wordEnd);
        
        ////grab random index then read two letters from there
        int twoRandomLetterStartIndex = (int) (Math.random() * secondWord.length() - 1); //take one off the end because consecutive
        System.out.println("Two random, consecutive letters from the second word");
        System.out.println(secondWord.substring(twoRandomLetterStartIndex, twoRandomLetterStartIndex + 2));

        //last word challenge
        ////get last word
        System.out.println("Last word with two letters switched");
        wordStart = spaceIndices.get(2) + 1; 
        String lastWord = testString.substring(wordStart); //assumes fourth word is final word

        ////get two random indices, then update the second until they are different
        int randLastWordIndex = (int) (Math.random() * lastWord.length());
        int randLastWordSecondIndex = randLastWordIndex;
        while (randLastWordIndex == randLastWordSecondIndex)
        {
            randLastWordSecondIndex = (int) (Math.random() * lastWord.length()); //no dups
        }

        ////make sure the first index comes first and second comes second
        if(randLastWordIndex > randLastWordSecondIndex)
        {
            int temp = randLastWordIndex;
            randLastWordIndex = randLastWordSecondIndex;
            randLastWordSecondIndex = temp;
        }

        ////put the new string together
        System.out.print(lastWord.substring(0, randLastWordIndex)); //string before first index
        System.out.print(lastWord.substring(randLastWordSecondIndex, randLastWordSecondIndex + 1)); //second index swap in
        System.out.print(lastWord.substring(randLastWordIndex + 1, randLastWordSecondIndex)); //string between indices
        System.out.print(lastWord.substring(randLastWordIndex, randLastWordIndex + 1)); //first index swap in
        System.out.print(lastWord.substring(randLastWordSecondIndex + 1)); //string after second index
    }
}
