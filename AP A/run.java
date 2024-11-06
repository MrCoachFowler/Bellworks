

public class run {
    public static void main(String[] args) 
    {
        IsPrime primeChecker = new IsPrime(183279324);
        System.out.println("The first method yields: " + primeChecker.isPrime1);
        System.out.println("The second method yields: " + primeChecker.isPrime2);
    }
    
}
