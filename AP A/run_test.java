


public class run_test {
    public static void main(String[] args)
    {
        boolean isT = true;
        boolean isntT = false;
        
        if(isT == true || isntT == true)
        {
            System.out.println("This works");
        }

        if(isT || !isntT)
        {
            System.out.println("Does this?");
        }
    }
}
