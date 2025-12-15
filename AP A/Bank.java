public class Bank {
        //Make attributes to store the following information:
    //account name
    //account balance
    //account password
    private String name;
    private double balance;
    private String password;

    //Create a Constructor
    public Bank(String name, String password)
    {
        this.name = name;
        this.password = password;
        this.balance = 0;
    }

    //Make a method following the contract
    //Name: deposit
    //Purpose: someone can add money to their balance
    //Input: amount of money to add
    //Output: void
    public void deposit(float addValue)
    {
        this.balance = this.balance + addValue;
    }

    //Make a method following the contract
    //Name: withdraw
    //Purpose: someone can take money from their balance
    //Input: amount of money to take
    //Output: void
    public void withdraw(float removeValue)
    {
        this.balance = this.balance - removeValue;
    }

    //write a run file that:
    //creates a new account for 'john' whose password is 'catlover123'
    //logs the accounts name and password
    //adds 20 dollars to the account
    //logs the account balance
    //removes 10 dollars from the account
    //logs the account balance

    //Challenge: prevent someone from overwithdrawing
}
