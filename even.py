'''
Author:IRENE
Date:22-11-24
'''
list1=[1,2,3,4]
list2=[5,6,7,8]
list_org=list1+list2
print("List 1=",list1)
print("list 2=",list2)
print("Merged list=",list_org)
even=[]
odd=[]
for numbers in list_org:
    if numbers%2==0:
        even.append(numbers)
        even.sort(reverse=True)
    else:
        odd.append(numbers)
        odd.sort(reverse=True)
print("Sorted list=",even+odd)