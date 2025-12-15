//without functional programming

var nums = [1, 2, 3]
for(var i = 0; i < nums.length; i++)
{
    nums[i] = nums[i] * 2
}
console.log(nums) //prints [2, 4, 6]

//with functional programming

var nums = [1, 2, 3]
var doubles = nums.map(num => 2 * num)
console.log(doubles) //prints [2,  4, 6]