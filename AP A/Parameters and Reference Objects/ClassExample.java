public class ClassExample
{
    private String val;

    public ClassExample() {this.val = "hello";}

    public String toString()
    {
        return this.val;
    }

    public void updateVal() {this.val += " world";}
}
