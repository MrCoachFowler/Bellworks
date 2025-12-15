

public class Die {
    private int value;

    public Die()
    {
        this.roll();
    }

    public void roll() {this.value = (int) (Math.random() * 6) + 1;}

    public int getValue() { return this.value; }
}
