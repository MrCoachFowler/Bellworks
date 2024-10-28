import java.util.ArrayList;

public class Test {
    public ArrayList<Question> questions = new ArrayList<Question>();
    public String id;
    public String subject;
    public int year;
    public String season;

    Test(String testId, String[][] questionRows)
    {
        this.id = testId;
        //break apart id by _ to isolate year, season, and subject
        //for each question in question rows....
            //make a new question object from the row
            //add it to the array list of questions
    }
}
