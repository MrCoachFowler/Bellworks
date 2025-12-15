<<<<<<< HEAD
public class Person {
    private String name;
    private String gender;
    private int age;

    public Person(String name, String gender, int age)
    {
        this.name = name;
        this.gender = gender;
        this.age = age;
    }

    public String toString()
    {
        String res = "Person: " + this.name + "\n";
        res += "Gender: " + this.gender + "\n";
        res += "Age: " + this.age;
        return res;
    }
}
=======
public class Person 
{
    String name;
    int id;
    String hairColor;

    public Person(String name, int id, String hairColor) //"Fowler", 1, "brown"
    {
        this.name = name;
        this.id = id;
        this.hairColor = hairColor;
    }
}


    //Make attributes to store the following information:
    //name
    //school session
    //type
    //answer choices
    //correct answers
    //score

    //make a constructor
    //updates name, type, and school session

    //Make a method following the contract
    //Name: scoreTest
    //Purpose: Compares the answers to the key
    //Input: test key answers
    //Output: void (updates correct answers and score)


    //write a run file that:
    //

>>>>>>> e0a5c590761ea29fd67c4ac8c762aea63c42de47
