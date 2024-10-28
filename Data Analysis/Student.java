import java.util.ArrayList;
public class Student {
    public String id;
    public ArrayList<TestResponse> testResponses = new ArrayList<TestResponse>();

    Student(String id)
    {
        this.id = id;
    }

    public void addNewTestResponse(TestResponse newTest)
    {
        this.testResponses.add(newTest);
    }

    
}
