'''
Author: Irene Jimmy
Date:18-10-24
Description:program that uses functions from the math module to perform the following operations on a number provided by the user
'''
import math
num=int(input("Enter a number"))
square_root=math.sqrt(num)
print("square root of",num,"=",square_root)
factorial_num=math.factorial(num)
print("Factorial of",num,"=",factorial_num)
power_2=math.pow(num,2)
print(num,"raised to the power 2=",power_2)
