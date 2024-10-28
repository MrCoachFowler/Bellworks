import java.util.ArrayList;

public class TestResponse {
    public String testId;
    public ArrayList<Answer> answers = new ArrayList<Answer>();
    public double score;
    public int weightedScore;

    TestResponse(String testId, String[] dataRow)
    {
        this.testId = testId;
        //set weighted score from specific place in dataRow
        //for each value in the data row, load the data into answer objects
    }

    public Test getTestInformation(ArrayList<Test> allTests)
    {
        for(Test test : allTests)
        {
            if(test.id.equals(this.testId))
            {
                return test;
            }
        }
        System.out.println("Cant find matching test?");
        return null;
    }

    public void score(Test referenceTest)
    {
        //compare each answer to each question of the reference test
        //set the isCorrect boolean for the answer objects
        //set the score attribute at the end
    }
    
}
