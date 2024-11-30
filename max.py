num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))
def number_max(num1,num2,num3):
    if (num1>num2) and (num1>num3):
        return num1

    elif(num2>num3):
        return num2
    else:
        return num3

print("Largest number=",number_max(num1,num2,num3))