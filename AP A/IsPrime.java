//your homework is to provide a 1 paragraph explanation why both of these methods are valid checkers for prime numbers
//use diagrams and drawings as necessary to make your point


public class IsPrime {
    boolean isPrime1;
    boolean isPrime2;

    public boolean isPrime1(int value)
    {
        int sqrt = (int) Math.sqrt(value);
        for(int i = 2; i <=sqrt; i++)
        {
            if(value % i == 0)
            {
                return false;
            }
        }
        return true;
    }

    public boolean isPrime2(int value)
    {
        for(int i = 2; i < value; i++)
        {
            if(value % i == 0)
            {
                return false;
            }
        }
        return true;
    }

    IsPrime(int value)
    {
        this.isPrime1 = isPrime1(value);
        this.isPrime2 = isPrime2(value);
    }
}
