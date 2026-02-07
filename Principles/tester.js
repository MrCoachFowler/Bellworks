function gradeFromPercentage(percentage)
{
    if (percentage >= 90) {return "A"}
    else if (percentage >= 80) {return "B"}
    else if (percentage >= 70) {return "C"}
    else if (percentage >= 60) {return "D"}
    else {return "F"}
}

let grade = gradeFromPercentage(74)
console.log(grade)

let fruit = "apple"
console.log(fruit) //fruits


let a_list = []
a_list[1]

let fruit1 = 'apple'
fruit1a = fruit1 + 's'
fruit1 += 's'
console.log(fruit1)
console.log(fruit1a)

let isHomeworkDone = true
let lastScore = 85

if(isHomeworkDone)
{
    console.log("Homeworks done!")
}
else
{
    console.log("Gotta do that homework")
}

if(lastScore >= 80)
{
    console.log("Atleast a B!")
}