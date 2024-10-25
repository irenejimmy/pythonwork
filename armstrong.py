'''
Author:Irene Jimmy
date:25-10-2024
description:Python program to find whether a number is armstrong or not.
'''
num=(int(input("Enter a number:")))

sum_of_digits=0
while num>0:
    remainder=sum_of_digits%10
    sum_of_digits=sum_of_digits+remainder**3
    num=num//10
if sum_of_digits==num:
    print("it is an armstrong number")
else:
    print("It is not an armstrong number")


