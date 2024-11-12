
public class main {
    public static void main(String[] args)
    {
        String qFileName = "C:\\Users\\tfowler\\Documents\\Comp Sci\\Repos\\Bellworks\\AP A\\Data Analysis\\data\\questions.csv";
        String aFileName = "C:\\Users\\tfowler\\Documents\\Bellworks\\AP A\\Data Analysis\\data\\answers.csv";
        CSVReader csv = new CSVReader(qFileName);


        //add test data from test info file
        String[] testNameFinder = qFileName.split("\\\\");
        String testNameWithCSV = testNameFinder[testNameFinder.length - 1];
        String testName = testNameWithCSV.split(".")[0];
        System.out.println(testName);


        for(int i = 7; i < csv.data.size(); i++)
        {
            String[] dataRow = csv.data.get(i);


        }
    }
}
