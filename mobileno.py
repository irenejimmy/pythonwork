'''
Author:Irene
Date:29-11-24
Description:Program to check whether the given number is a valid mobile number or not using functions.
'''
def valid_mobile_num(number):

    if len(number)==10 and number[0] in ["9","8","7"]:
        return True
    return False

number=input("Enter mobile number:")
if valid_mobile_num(number):
    print("It is valid")
else:
    print("It is invalid")