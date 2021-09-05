# #for loop
#
# num=int(input("enter a number :"))
# fac=1
#if num>0:
#   for i in range(1,num+1):
#     fac=fac*i
#   print(fac)
# elif num==0:
#     print("fac=1")
# else:
#     print("not a positive number")

#while loop
num=int(input("enter a number :"))
fac=1
i=1
if num>0:
    while (i<=num):
       fac=fac*i
       i+=1
    print(fac)
elif num==0:
    print("fac=1")
else:
    print("not a positive number")
