# * ARGS
#-------

# def xyz(a,b):
#     return a,b
# print(xyz(2,8))  #if in this case when we using more than number of values given...it will show error (2,8,6)

# so we use star args

# def xyz(*args):
#     return args
# print(xyz(1,6,3,25,5))   #output of star args will be TUPLE



# ** ARGS
#---------

# def xyz(**args):
#     return args
# print(xyz(name="ANU",age=22,place="KOCHI"))     #OUTPUT WILL BE DICTIONARY


# Q...USING * ARGS---CALCULATE SUM OF GIVEN VALUES

# def num(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(num(1,2,3,4,5,6))



# def num(*args):
#     return sum(args)
# print(num(1,2,3,4,5,6))

# def num(*args):
#     return sum(args)     #USING IN BUILT KEYWORD
# print(num(10,3,40))

