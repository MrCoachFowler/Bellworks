import java.time.LocalDate;
import java.util.ArrayList;

public class BirthdayMatchPerson {
    
    private String birthday;

    public BirthdayMatchPerson()
    {
        int year = 2025; // you can change this to any year
        int dayOfYear = (int) (Math.random() * 365) + 1;
        LocalDate randomDate = LocalDate.ofYearDay(year, dayOfYear);

        this.birthday = randomDate.toString();

int rowCount = 3;
int colCount = 5;
ArrayList<ArrayList<String>> sArray = new ArrayList<>();
for(int row = 0; row < rowCount; row++)
{
    sArray.add(new ArrayList<String>());
    for(int col = 0; col < colCount; col++)
    {
        sArray.get(row).add("Hi");
    }
}
    }

    public String getBirthday() { return this.birthday; }
}
