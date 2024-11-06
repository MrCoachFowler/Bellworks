import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class CSVReader {
    public ArrayList<String[]> data = new ArrayList<>();

    CSVReader(String fileName) 
    {
        try
        {
            File f = new File(fileName);
            String delimiter = ",";

            Scanner s = new Scanner(f);
            while(s.hasNextLine())
            {
                String line = s.nextLine();
                String[] values = line.split(delimiter);
                data.add(values);
            }

            for(String[] line : this.data)
            {
                for(String value : line)
                {
                    System.out.print(value + ", ");
                }
                System.out.println();
            }
            
        } catch (FileNotFoundException e)
        {
            System.out.println("Couldnt read file");
        }
        
    }
}