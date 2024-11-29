'''
Author:Irene
Date:29-11-24
Description:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.


'''


def right_triangle(side):
    side.sort()
    if side[2]**2==side[0]**2+side[1]**2:
        return True
    return False


side=[]
side.append(int(input("Enter length of side 1")))
side.append(int(input("Enter length of side 2")))
side.append(int(input("Enter length of side 3")))
if right_triangle(side):
    print("It is right angled triangle")
else:
    print("It is not a right angled triangle")
