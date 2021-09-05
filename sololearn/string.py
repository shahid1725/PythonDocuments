
#1
# for i in range(0,6):
#     for i in range(i):
#         print("1",end=" ")
#     print("\r")
# for i in range(5,0,-1):
#     for i in range(i):
#         print("2",end=" ")
#     print("\r")
# for i in range(0,6):
#     for i in range(i):
#         print("3",end=" ")
#     print("\r")
# for i in range(5,0,-1):
#     for i in range(i):
#         print("4",end=" ")
#     print("\r")

#2..

# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# dup = []
# [dup.append(x) for x in lst if x not in dup]
# print ("The list after removing duplicates : " ,dup)

#3..
# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print(lst[-2])

#4..
# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# common=[]
# for i in a:
#     for j in b:
#         if i==j:
#             common.append(i)
# print(common)

#6
# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def multi(num1,num2):
#     return (num1*num2)
# def divi(num1,num2):
#     return num1/num2
# def floor(num1,num2):
#     return (num1//num2)
# def exponent(num1,num2):
#     return num1**num2
# print("CALCULATOR")
# print("press\n1.ADDITION\n2.SUBSTRACTION\n3.DIVISION\n4.MULTIPLICATION\n5.FLOOR DIVISION\n6.EXPONENT")
#
# while True:
#     choice=int(input("enter your choice :"))
#     num1=float(input("enter first number : "))
#     num2=float(input("enter second number: "))
#     if 0>choice or choice>6:
#         print("Invalid Choice")
#     elif choice==1:
#         print(add(num1,num2))
#     elif choice==2:
#         print(sub(num1, num2))
#     elif choice==3:
#         print(divi(num1, num2))
#     elif choice==4:
#         print(multi(num1,num2))
#     elif choice==5:
#         print(floor(num1,num2))
#     elif choice==6:
#         print(exponent(num1,num2))
#

#6..
# def sumprimes(n):
# sum1 = 0
# for i in range(1,len(n)):
#     num = n[i]
#     if num > 1:
#         prime = True
#         for j in range(2, int(num**0.5)+1):
#             if num%j == 0:
#                 prime = False
#                 break
#         if prime:
#             sum1 = sum1 + num
#         #else:
#         #    sum1 = 0
# return(sum1)
# print(sum)
# for a in range(min,max+1):
#     if a>1:
#         for i in range(2,a):
#             if a%i==0:
#                 break
#         else:
#             print(a)



#7
# user=input("enter your string :")
# vowels="aeiouAEIOU"
# for i in user:
#     if i in vowels:
#         newstr=user.replace(i)
# print(newstr)

#8
# in python we use functions in programming to get a set of instructions that we want to use repeatedly

#9
# LIST
# 1.KEEPING ORDER
# 2.SUPPORT DUPLICATION
# 3.heterogenious
# 4.nesting possible
# 5.LIST IS MUTABLE
#
# SET
# 1.set doesn't keep order
# 2.heterogenious
# 3.set doesn't support duplicate elements
# 4.nesting not possible
# 5.set is mutable

#10
# List comprehension in Python is an easy and  syntax for creating a list from a string or another list.
# LIST=[i for i in range(1,101,1) if i%5==0]
# print(LIST)

#11
# append() method in python adds a single item to the existing list
# list=[1,2,3,4]
# list.append(5)
# print(list)
#
# extend(): Iterates over its argument and adding each element to the list and extending the list
# list=[6,7,8,9]
# L=["hello","hi"]
# list.extend(L)
# print(list)




#
# def is_leap(year):
#     if year%4==0:
#         return True
#     elif year%100==0:
#         return False
#     elif year%400==0:
#         return True
#     if year%4!=0:
#         return False

students= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort()
print(students)

