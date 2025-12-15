
import java.util.ArrayList;

public class Helper
{
    public static void stringListSort(ArrayList<String> arr)
    {
        //This should modify the arr argument in place to be sorted
        //Hint: you'll want to get a little used to the compareTo method
    }

    public static void main(String[] args)
    {
        ArrayList<String> test_list = new ArrayList<>();
        test_list.add("one");
        test_list.add("two");
        test_list.add("three");
        test_list.add("four");

        stringListSort(test_list);
        System.out.println("The ArrayList after sorting: ");
        for(String word : test_list)
        {
            System.out.print(word + " ");
        }
        //Should be: four one three two
    }
}