'''
Author: Irene Jimmy
Date:18-10-24
Description:program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results.
'''
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=num1+num2
print("a=",num1)
print("b=",num2)
num4=num1/num2
print("sum=", num3,",""Division=",num4)
num1>num2
print("Is a greater than b?: True")
num1!=num2
print("Are a and b equal?:False")
print("Logical AND:",num1>0 and num2>0)
print("Logical OR:",num1>0 and num2>0)