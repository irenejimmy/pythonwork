'''
Author:Irene
Date:29-11-24
Description:Recursive function to multiply two positive numbers
'''
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
def recursive_mul(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_mul(num1,num2-1)
print(recursive_mul(num1,num2))