
import java.util.ArrayList;

public class Helper
{
   public static void stringListSort(ArrayList<String> arr)
   {
        //This should use an insertion sort algorithm to return a sorted list
        for(int i = 1; i < arr.size(); i++)
        {
            String targetWord = arr.get(i);
            int placeIndex = i;
            while(placeIndex > 0 && targetWord.compareTo(arr.get(placeIndex - 1)) < 0)
            {
                placeIndex -= 1;
            }

            if (placeIndex != i)
            {
                arr.remove(i);
                arr.add(placeIndex, targetWord);
            }
        }

   }

   public static void main(String[] args)
   {
        ArrayList<String> test_list = new ArrayList<>();
        test_list.add("one");
        test_list.add("two");
        test_list.add("three");
        test_list.add("four");

        stringListSort(test_list);
        for(String word : test_list)
        {
            System.out.print(word + " ");
        }
   }
}