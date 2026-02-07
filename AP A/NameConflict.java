public class NameConflict {
    private String name;
    private int age;

    public NameConflict(String n, int age)
    {
        this.name = n;
        this.age = age;
    }

    
    public String helloWorld(int num)
    {
        System.out.println(num);
        return "Hello World";
    }

    public int squareArea(int s)
    {
        //multiply s by itself
        //return result
    }
    //public <return_data type> <function name>( <input data type> <input variable name>, ...)
}
