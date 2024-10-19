'''
Author:Irene Jimmy
Date:19-10-24
Description:Simple desktop calculator using Python. Only the five basic arithmetic operators.
'''
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

num3=int(input("Enter a number"))

sum=num1+num2
print("The sum of num1 and num2 is:",sum)

sub=num2-num1
print("The difference when num2 is subtracted from num1 is: ",sub)

mul=num1*num2
print("The product of num1 and num2 is: ",mul)

div=num1/num2
print("The quotient when num1 is divided by num2 is:",div)

mod=num1%num2
print("The remainder when num1 is divided by num2 is:",mod)

result = (num1 + num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is: ",result)