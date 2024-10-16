//Create a function following this contract:
//Name: speller
//Purpose: take in any word and spell it out
//Input: word (string)
//Output: void
function speller(word)
{
    for(let i = 0; i < word.length; i++)
    {
        console.log(word[i]);
    }
}

//Create a function following this contract:
//Name: reverseSpeller
//Purpose: take in any word and spell it backwards
//Input: word (string)
//Output: void
function reverseSpeller(word)
{
    for(var i = 1; i <= word.length; i++)
    {
        console.log(word[word.length - i]);
    }
}



//Create a program that:
//spells out "supercalifragilisticexpialidocious"
//spells out "supercalifragilisticexpialidocious" backwards
//spells your name backwards
speller("supercalifragilisticexpialidocious");
reverseSpeller("supercalifragilisticexpialidocious");
reverseSpeller("mr coach fowler");

//challenge: do it all in one line by creating and appending to a string
