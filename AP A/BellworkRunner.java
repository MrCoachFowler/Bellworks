public class BellworkRunner {
    public static void main(String[] args) {
        {
            Bank account = new Bank("John", "CatLover123");
            System.out.println("name: " + account.name + ", password: " + account.password);
            account.deposit(20);
            System.out.println(account.balance);
            account.withdraw(10);
            System.out.println(account.balance);
        }
    }
}
