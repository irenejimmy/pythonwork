'''
Author:Irene Jimmy
Date:19-10-24
Description:Create, concatenate, and print a string and access a sub-string from a given string.
'''
str_1=input("Enter your first name")
str_2=input("Enter your second name")
str_3=str_1 +" "+ str_2
print(str_3)
length_str1=len(str_1)
print(length_str1)
extracted_str_2=str_3[length_str1+1:]
print(extracted_str_2)
