public class run {
    public static void main(String[] args) 
    {
        ShapePrinter printer = new ShapePrinter();
        printer.printShape(8, "rectangle");
        System.out.println();
        printer.printShape(5,"right triangle");
        System.out.println();
        printer.printShape(4,"left triangle");
    }
    
}
