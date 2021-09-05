# num=int(input("enter a number :"))
# if num>0:
#
#     if num%2==0:
#         print("positive number")
#     else:
#         print("negative number")
# else:
#     print("invalid number..pls choose positive number")
#
#

min=int(input("enter a min number :"))
max=int(input("enter a mx number:"))

for i in range(min,max):
    if i%2==0:
        print(i,"positive number")
    else:
        print(i,"negative number")
