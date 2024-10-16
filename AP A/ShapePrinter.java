

public class ShapePrinter {
    //Make attributes to store the following information:
    //NA

    
    //make a constructor
    //empty
    ShapePrinter()
    {
        //pass
    }

    //Make a method following the contract
    //Name: printShape
    //Purpose: print a rectangle, left triangle, or right triangle out of " - "
    //Input: base length and shape type
    //Output: void
    public void printShape(int size, String shape)
    {
        if(shape.equals("rectangle"))
        {
            String row = new String();
            for(int i = 0; i < size; i++)
            {
                row += " - ";
            }

            for(var i = 0; i < size; i++)
            {
                System.out.println(row);
            }


        }

        else if (shape.equals("right triangle"))
        {
            //one row at a time
            for(int row = 0; row < size; row++)
            {
                String text = new String();
                //build the text for the row into a string
                for(int col = 0; col < size; col++)
                {
                    //add blank space if not in triangle
                    if(col >= size - 1 - row)
                    {
                        text += " - ";
                    }
                    //line if in triangle
                    else
                    {
                        text += "   ";
                    }
                }
                //print the row
                System.out.println(text);
            }

        }

        else if(shape.equals("left triangle"))
        {
            //one row at a time
            for(int row = 0; row < size; row++)
            {
                String text = new String();
                //build the text for the row into a string
                for(int col = 0; col < size; col++)
                {
                    //add blank space if not in triangle
                    if(col <= row)
                    {
                        text += " - ";
                    }
                    //line if in triangle
                    else
                    {
                        text += "   ";
                    }
                }
                //print the row
                System.out.println(text);
            }
        }

        else 
        {
            System.out.println("Shape not recognized");
        }
    }

    //write a test file that:
    //prints a left triangle of size 4
    //prints a right triangle of size 5
    //prints a rectangle of size 8
}
