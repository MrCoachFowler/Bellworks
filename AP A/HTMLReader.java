
import java.util.ArrayList;

public class HTMLReader {
    //Make attributes to store the following information:
    //
    public String html;

    
    //make a constructor
    public HTMLReader(String html)
    {
        this.html = html;
    }

    //Make a method following the contract
    //Name: 
    //Purpose: 
    //Input: 
    //Output:
    public ArrayList<String> getHTags()
    {
        int startIndex = 0;
        ArrayList<String> res = new ArrayList<>();

        startIndex = this.html.indexOf("<h1>");
        while(startIndex != -1)
        {
            int endIndex = this.html.indexOf("</h1>", startIndex);
            res.add(this.html.substring(startIndex + 4, endIndex));
            startIndex = this.html.indexOf("<h1>", endIndex);
        }
        return res;
    }

    //write a test file that:
    //
}
