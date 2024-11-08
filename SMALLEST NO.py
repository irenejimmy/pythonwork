'''
Author:Irene
Date:08-11-24
Description:Program to find the largest and smallest number among a list of numbers
'''
limit=int(input("Enter a limit"))
num=int(input("Enter a number"))
small=num
big=num
while limit>1:
    num=int(input("Enter a number"))
    if num>big:
        big=num
    elif num<small:
        small=num
    limit=limit-1
print("Big=",big)
print("Small=",small)

