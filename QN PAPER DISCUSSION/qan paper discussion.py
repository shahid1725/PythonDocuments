#Q..1
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# 2 2 2 2 2
# 2 2 2 2
# 2 2 2
# 2 2
# 2
# 3
# 3 3
# 3 3 3
# 3 3 3 3
# 3 3 3 3 3
# 4 4 4 4 4
# 4 4 4 4
# 4 4 4
# 4 4
# 4
# a=int(input("enter initial range"))
# b=int(input("enter final range"))
# r=5
# for i in range(a,b):
#     if(i%2==0):
#
#         #print(i)
#         for k in range(r,0,-1):
#             for j in range(0,k):
#                 print(i,end="")
#             print("\r")
#
#     else:
#         for l in range(r):
#             for m in range(0,l+1):
#                 print(i,end="")
#             print("\r")
#
#


# #Q2..lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]  ELIMINATE DUPLICATE ELEMENTS IN ONE LINE
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# #convert to list then set to list
# print(list(set(lst)))

#Q3..
#Q...FIND SECOND LARG ELEMENT
# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print(lst[-2])

#Q..4
#.create a function with arguments and return type which find sum of prime numbers between 1 - 50?
def sumprime(min,max):
    sum=0
    for a in range(min,max):
        if a>1:
            for i in range(2,a):
                if(a%i)==0:
                    break
            else:
                sum=sum+a
    return sum
print(sumprime(1,10))