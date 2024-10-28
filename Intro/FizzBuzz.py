#Make a function based on the following contract:
#Name: fizzBuzz
#Purpose: Count to a specified number
##if the number is divisible by 3, print "fizz" instead
##if the number is divisible by 5, print "buzz" instead
##if the number is divisible by 3 and 5, print "fizzbuzz" instead
#Input: number to count to
#Output: void
def fizzBuzz(maxNum):
    for i in range(maxNum + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#write a program that:
#fizzbuzz to 15
#fizzbuzz to 30
#fizzBuzz to 1000
fizzBuzz(15)
fizzBuzz(30)
fizzBuzz(1000)