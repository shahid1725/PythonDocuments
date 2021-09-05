# list=[1,2,3,4,5,1,2,3]
# print(list)             #1..KEEPING ORDER
#                         #2..SUPPORT DUPLICATION
# print(type(list))
# for i in list:
#     print(i)

# list2=["hello",1,15,85,"hi",True]
# print(list2)            #3..heterogenious(can store diffrnt types of data ...strng,bool,float..

# list=[]
# list.append("hello")       #append is the keyword to add elements to list
# list.append(1)
# print(list)

#Q.ASK USER SIZE OF LIST, THEN ADD ELEMENTS FROM USER

# num=int(input("enter number of elements :"))
# list=[]
# for i in range(num):
#     z=int(input("enter number:"))
#     list.append(z)
# print(list)

#NESTING
# lst=[1,2,5,[4,5,8,[2,0,4]]]
# print(lst)                      #4.....nesting possible

#UPDATION

# LIST=[1,2,3]
# LIST.append(5)                     #append---add elemnts
# LIST.remove(2)                     #REMOVE---REMOVE SPECIFIC ELEMENT
# LIST.clear()                       #CLEAR---remove full elements
# del LIST                           #DEL-----to delete list
# print(LIST)                       #5.......LIST IS MUTABLE

#Q.CREATE A LIST OF SQUARES FROM BELOW LIST
# list=[1,2,3,4,5,6]
# listsqr=[]
# for i in list:
#     z=i**2
#     listsqr.append(z)
# print(listsqr)

#LINEAR SERACH
#Q-----SEARCH AN element from list that user entered---------

# lnr=[2,5,8,7,4,6,8,8,4,2,1,5,88,6,6,99]
# def linearsearch(lnr):
#     element=int(input("enter element to search :"))
#     fla=0
#     for i in lnr:
#         if i==element:  #or if in lnr
#             fla=1
#             break
#     if fla==0:
#         print("not found")
#     else:
#         print("found")
# linearsearch(lnr)

#Q. SUM OF LIST
# list=[1,5,2,3]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

#LIST TRAVERSING
#---------------
# list=[1,2,5,6,2,5,8]
# print(list[0])          #index number
# print(list[-1])
# print(list[2:5])

#SORT
#----

# mylist=[89,5,8,15,45,2,3,69]
# mylist.sort()               #sort----arranging elements
# print(mylist)

#Q.ARRANGE ORDER OF ELEMENTS
# mylist=[2,5,8,66,4,58,22,833,66,99,88]
# newlist=[]
#
# while mylist:
#     min=mylist[0]
#     for i in mylist:
#         if i<min:
#             min=i
#     newlist.append(min)
#     mylist.remove(min)
# print(newlist)
# print(mylist)

#SLICING
#----------

# list=[1,2,3,6,5,4,8,5]
# print(list[1:3])
# print(list[-4:-1])
# print(list[:4])
# print(list[3:])
# print(list[:])
# print(list[1:5:2])
# print(list[::-1])   #reverse

#Q.FIND DUPLICATE ELEMENTS
# list=[1,2,5,8,6,9,10]
# list2=[2,5,8,66,33,0,10]
# dup=[]
# for i in list:
#     for j in list2:
#         if i==j:
#             dup.append(i)
# print(dup)

# list=[1,2,5,8,6,8,5,2,3]
# dup=[]
# for i in list:
#     if i not in dup:
#         dup.append(i)
#     else:
#         print(i)

#Q. FIND MIN AND MAX FUNCTION OF LIST
#
# list=[10,2,5,9,66,23,1,22]
# list.sort()
# print(list)
# print("min element :",list[0])      #min element
# print("max element :",list[-1])      #max element

#Q.CREATE A LIST,FIND THE RESULTS OF ELEMENT MULTIPLIED WITH 5
# list=[1,2,5,6,8,9,6,4,2]
# ml=[]
# for i in list:
#     z=i*5
#     ml.append(z)
# print(ml)

        #or USING LIST COMPREHENSION
# list=[1,2,5,6,8,9,6,4,2]
# ml=[i*5 for i in list]
# print(ml)

#Q.odd / even using LIST COMPREHENSION
# list=[1,2,3,4,5,6,7,8,9]
# odd=[n for n in list if n%2!=0]
# print("odd numbers :",odd)
#
# even=[n for n in list if n%2==0]
# print("even numbers:",even)

#Q.use list comp,create list with even  numbers bw 100-200
# list=[i for i in range(100,201,2) ]
# print(list)

        #or
# even=[i for i in range(100,200) if i%2==0]
# print(even)

#Q.multiply the elements from the list with input
# num=int(input("enter a number to multiply :"))
# list=[1,2,3,4,5,6,7,8,9]
# multi=[]
# for i in list:
#     z=i*num
#     multi.append(z)
# print(multi)

#Q.multiply All list elemenet each other

# list=[1,2,3,4,5]
# s=1
# for i in list:
#     s=s*i
# print(s)

#BINARY SEARCH
#--------------
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#
# def bsearch():
#     list.sort()
#     print(list)
#     ele=int(input("enter element:"))
#     fla=0
#     low=0
#     upp=len(list)-1
#     while low<=upp:
#         mid=(low+upp)//2
#
#         if ele>list[mid]:
#             low=mid+1
#         elif ele<list[mid]:
#             upp=mid-1
#         elif ele==list[mid]:
#             print(mid)
#             fla=1
#             break
#     if fla==1:
#         print("found")
#     else:
#         print("not found")
#
# bsearch()

#updation of list using index position
#------------------------------------

# a=[1,5,9,8,7,4,5]
# a[0]=3,
# print(a)

#append
#------
# list=['hi','kooi']
# a=[1,3,6,5,4]
# list.append(a)              #append - add  for nested
# print(list)

#extend
#------
# list=['hi','kooi']
# a=[1,3,6,5,4]
# list.extend(a)                  #extend for add
#
# print(a)


# lis=[1,5,6,9,8]
# m=['j','l']
# lis.extend(m)
# print(lis)