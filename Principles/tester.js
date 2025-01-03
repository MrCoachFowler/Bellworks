function decideColor(genetics)
{
    if (genetics.includes("r"))
    {
        if (genetics.includes("w"))
        {
            return "pink"
        }
        else
        {
            return "red"
        }
    }
    else
    {
        return "white";
    }
}

console.log(decideColor("rr"))