// function gradeFromPercentage(percentage)
// {
//     if (percentage >= 90) {return "A"}
//     else if (percentage >= 80) {return "B"}
//     else if (percentage >= 70) {return "C"}
//     else if (percentage >= 60) {return "D"}
//     else {return "F"}
// }

// let str1 = "user@domain.tld"

// let atIndex = str1.indexOf("@");
// let domainSeperator = str1.indexOf(".");

// console.log(atIndex);
// console.log(domainSeperator);

// console.log(str1.substring(0, atIndex));
// console.log(str1.substring(atIndex + 1, domainSeperator));

// for(let i = 0; i < 5; i++)
// {
//     //do stuff
// }

// let i = 0;
// while (i < 5)
// {
//     //do stuff
//     i++
// }

// //potato object creation
// let needsMorePeeling = true
// while(needsMorePeeling)
// {
//     potato.peel()
//     if(potato.isPeeled())
//     {
//         needsMorePeeling = false
//     }
// }

// let an_array = [1, 2, 3, 4, 5, "a", "b", "c"]
// for(let i = 0; i < an_array.length; i++)
// {
//     console.log(an_array[i])
// }

function returnTrue()
{
    console.log("Hello")
    return true
}
function returnFalse()
{
    console.log("World")
    return false
}

if(returnFalse() & returnTrue())
{
    console.log("Version one was true")
}

if(returnFalse() && returnTrue())
{
    console.log("Version two was true")
}

// if(returnTrue() | returnFalse())
// {
//     console.log("Version one was true")
// }

// if(returnTrue() || returnFalse())
// {
//     console.log("Version two was true")
// }