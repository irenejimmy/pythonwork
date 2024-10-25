'''
Author:Irene Jimmy
date:25-10-2024
description:Python program to convert temperature values back and forth between Celsius and Fahrenheit.
'''
temp1=int(input("Enter temperature:"))

scale=input("Is this in (C)elisus or (F)arenheit")
if scale=="c":
    f = (9/5*temp1) + 32
    print(temp1,"Celsius is ",f, "Fahrenheit.")
else:
    c = 5/9*(temp1-32)
    print(temp1,"farenheit is",c,"celisus")





