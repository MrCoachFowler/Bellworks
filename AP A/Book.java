public class Book
{
    private String title;
    private String genre;
    private String author;
    private int numPages;

    
    public Book()
    {
        // title = "";
        genre = "";
        author = "";
        // numPages = 0;
    }

    /** Method to construct a Book object
     * @param t - title of book
     * @param g - genre of book
     * @param a - author of book
     * @param n - page number of book
     */
    public Book(String t, String g, String a, int n)
    {
        title = t;
        genre = g;
        author = a;
        numPages = n;
    }

    public String getTitle()
    {
        return title;
    }

    public int getNumPages()
    {
        return numPages;
    }
}

