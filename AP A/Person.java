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
