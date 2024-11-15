import random
my_list=list(range(1,11))
for i in my_list:
    print (i,end=' ')
my_list[4]=20
print (my_list)
random_number=ramdom.choice(my_list)
print(random_number)