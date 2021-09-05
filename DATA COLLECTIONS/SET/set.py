#to store elements....
# a={1,2,3,4,5,6}
# print(a)
# print(type(a))
# b={7,8,9}
# print(b)

#empty set
# a=set()
# a.add(2)        #"add" keyword to add element to set
# a.add(6)
# a.add(1)        #1..set doesn't keep order
# a.add("hello")
# a.add(0.25)
# a.add(-2)
# a.add(True)    #2..heterogenious(can store diffrnt types of data ...strng,bool,float..
# print(a)

# a={1,2,3,1,2}
# print(a)        #3..set doesn't support duplicate elements


# B={5,4,False}
# for i in B:
#     print(i)

#Q.ask set size from user and add elements to sets
# a=set()
# num=int(input("how much number do you want to add :"))
# for i in range(num):
#     z=int(input("enter number"))
#     a.add(z)
# print(a)

#Q. create a set of B which is the square of set A
# a={1,2,3,4,5,6}
# b=set()
# for i in a:
#     z=i**2
#     b.add(z)
# print(b)

#4..set is mutable (can update elements)
# s={1,2,3,4,5,6,7,8,9}
# s.remove(5)     #to remove a specific element
# print(s)
#
# s.clear()       #to remove total elements
# print(s)

                 #del             #to remove empty set

#5..nesting not possible
    #a={1,2{3,4}}
    #print(a)

#Q.make sets of odd n even numbers from given set
# set1={1,2,3,4,5,6,7,8,9,10}
# odd=set()
# even=set()
# for i in set1:
#     if i%2==0:
#         even.add(i)
#
#     else:
#         odd.add(i)
# print(even,odd)

#Q.find common elements from sets
# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8,9,10}
# common=set()
# for i in s1:
#     if i in s2:
#         common.add(i)
# print(common)

                    #UNION
                    #INTERSECTION
                    #DiFERENCE

# a={1,2,3,4,5,6,7}
# b={4,5,6,1,2,5,8,}
# print(a.union(b))       #for total elements
# print(a.intersection(b)) #for common elements
# print(a.difference(b))    #a-b

#Q.Create sets for PRIME NUMBERS AND NON PRIME NUMBERS FROM BELOW SETS
# s={1,2,3,4,5,6,7,8,9}
# prime=set()
# nonprime=set()
# for i in s:
#     if i>1:
#         for j in range(2,i):
#             if(i%j)==0:
#                 nonprime.add(i)
#                 break
#             else:
#                 prime.add(i)
# print(prime)
# print(nonprime)

