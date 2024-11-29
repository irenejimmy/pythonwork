'''
Author:Irene
Date:29-11-24
Description:Recursive function to add two positive numbers.
'''
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
def recursive_add(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)
print(recursive_add(num1,num2))
