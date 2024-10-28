public class Answer {
    public double time;
    public String answer;
    public boolean isCorrect;

    Answer(double time, String answer)
    {
        this.time = time;
        this.answer = answer;
    }

    public void setCorrectness(boolean isCorrect)
    {
        this.isCorrect = isCorrect;
    }
}
