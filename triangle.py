'''
Author:IRENE
Date:22-11-24
row=int(input("Enter number of rows"))
'''
for i in range (row):
    for j in range(i+1):
        print("*",end="")
    print("")

row=int(input("Enter the number of rows"))
print("decreasing triangle")

for i in range (row):
    for j in range(row-i):
        print("*",end="")

    print(" ")
print("hill pattern")


row=int(input("Enter the number of rows"))
for i in range(1, row +1):
    for j in range(row - i):
        print(" ",end="")
    for k in range (2*i-1):
        print("*", end="")
    print()

row=int(input("Enter the number of rows"))
print("reverse hill pattern")

for i in range(row,0,-1):
    for j in range (row - i):
        print(" ",end="")
    for k in range (i*2-1):
        print("*",end="")
    print()