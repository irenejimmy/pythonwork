'''
Author:Irene Jimmy
Date:28-10-2024
Description:Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:
Convert Celsius to Fahrenheit
Convert Fahrenheit to Celsius
Exit the program
'''
while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        temp1=float(input("Enter temperature in celsius:"))
        cel_far=(temp1* 9/5) + 32
        print(temp1,"C in fareheit is",cel_far,"F")
    elif choice==2:
        temp2=float(input("Enter temperature in Fahrenheit:"))
        far_cel=(temp2 - 32) * 5/9
        print(temp2,"F in Celsius is",far_cel,"C")
    elif choice==3:
        break
    else:
        print("Invalid Entry")


