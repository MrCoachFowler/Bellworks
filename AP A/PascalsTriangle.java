import java.util.ArrayList;

public class PascalsTriangle {
    //Make attributes to store the following information:
    //triangleSize
    int triangleSize;
    ArrayList<ArrayList<Integer>> coefficents;

    
    //make a constructor
    //sets triangle highest power
    PascalsTriangle(int power)
    {
        this.triangleSize = power + 1;
        this.createCoefficientArrayList();
    }

    //Make a method following the contract
    //Name: createCoefficientArrayList
    //Purpose: stores an arraylist of cofficients for the triangle as an attribute
    //Input: void
    //Output: void
    public void createCoefficientArrayList()
    {
        //create an arraylist to store the rows of the triangle
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        for(int rowIndex = 0; rowIndex < this.triangleSize; rowIndex++)
        {
            //create an arraylist for the row
            ArrayList<Integer> row = new ArrayList<Integer>();

            //if its the first row, use 1 and move on
            if(rowIndex == 0)
            {
                row.add(1);
            }
            //if its the second row, add two ones and move on
            else if (rowIndex == 1)
            {
                row.add(1);
                row.add(1);
            }
            //if its after that, start with 1, then add the sum of previous rows, then add a 1
            else 
            {
                row.add(1);

                int lastRowIndex = result.size() - 1;
                ArrayList<Integer> prevRow = result.get(lastRowIndex);
                for(int i = 0; i < lastRowIndex; i++)
                {
                    row.add(prevRow.get(i) + prevRow.get(i + 1));
                }

                row.add(1);

            }

            result.add(row);
        }
        this.coefficents = result;
    }
    

    //Make a method following the contract
    //Name: printCoefficients
    //Purpose: prints out the coefficients of a pascals triangle
    //Input: void
    //Output: void
    public void printCoefficients()
    {
        for(int i = 0; i < this.coefficents.size(); i++)
        {
            ArrayList<Integer> row = this.coefficents.get(i);
            for(Integer coefficient : row)
            {
                System.out.print(coefficient + " ");
            }
            System.out.println();
        }
    }


    //write a test file that:
    //prints out a pascals triangle to the 4th exponent
    //prints out a pascals triangle to the 8th exponent
    //prints out a pascals triangle to the 15th exponent
}
