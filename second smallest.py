limit=int(input("Enter a limit"))
num=int(input("Enter a number"))
small=num
second_small=small
big=num
second_big=big
while limit>1:
    num=int(input("Enter a number"))
    if num>big:

        second_big=big
        big=num
    elif num>second_big:
        second_big=num
    if num<small:
        second_small=small
        small=num


    elif num<second_small:
        second_small=num
    limit=limit-1
print("Second Big=",second_big)
print("Second Small=",second_small)
