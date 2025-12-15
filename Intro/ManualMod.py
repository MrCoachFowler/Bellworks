import math

#Make a function based on the following contract:
#Name: manualMod
#Purpose: Given two numbers, A and B, find A % B
#Input: two positive integers
#Output: the modulus of the first number by the second
def manualMod1(A, B):
    while A >= B:
        A -= B
    return A

def manualMod2(A, B):
    multiTimes = math.floor(A / B)
    return A - B * multiTimes


#write a program that:
# Calculates 14 % 2 (0)
print(manualMod1(14, 2))
print(manualMod2(14, 2))
# Calculates 25 % 7 (4)
print(manualMod1(25, 7))
print(manualMod2(25, 7))
# Calculates 123452353 % 29382 (18571)
print(manualMod1(123452353, 29382))
print(manualMod2(123452353, 29382))