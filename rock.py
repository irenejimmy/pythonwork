'''
author:irene
date:15.11.24
description:program to play rock paper scissors
'''

import random
my_list=['rock','paper','scissors']
com_choice=random.choice(my_list)
my_choice=input("Enter your choice:")
print(my_choice)
print("Computer choice is",com_choice)
if com_choice==my_choice:
    print("It's a tie")
elif com_choice=='rock' and my_choice=='paper':
    print("Computer wins")
elif com_choice=='paper' and my_choice=='rock':
    print("You Win")
else:
    print("you win")
