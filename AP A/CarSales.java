public class CarSales {
    public String model;
    public String owner;
    public boolean isSportsCar;

    public CarSales(String model, String owner, boolean isSportsCar)
    {
        this.model = model;
        this.owner = owner;
        this.isSportsCar = isSportsCar;
    }

    public CarSales(String model, boolean isSportsCar)
    {
        this.model = model;
        this.owner = null;
        this.isSportsCar = isSportsCar;
    }
}