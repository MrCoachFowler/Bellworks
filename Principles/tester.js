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