#  M A P

lst=[2,3,4,5,6]

#print squares of all numbers

# def sqaure(num):
#     return num**2
# squares=list(map(sqaure,lst)) #in MAP we have to use 2 arguments , first is function , second iterable
# print(squares)

#print cube of numbers
# def cube(num):
#     return num**3
# cubes=list(map(cube,lst))
# print(cubes)

# in lambda
# cube=lambda num:num**3
#SO WE CAN REDUCE THE CODE BY USING LAMBDA

# cubes=list(map(lambda num:num**3,lst))
# print(cubes)

#in sqaure case

# squares=list(map(lambda num:num**2,lst))
# print(squares)

employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id": 1001, "e_name": "joju", "salary": 20000, "department": "operating", "exp": 1},
    {"e_id": 1002, "e_name": "raju", "salary": 15000, "department": "experting", "exp": 0},
    {"e_id": 1003, "e_name": "ramu", "salary": 11000, "department": "marketing", "exp": 2},
    {"e_id": 1004, "e_name": "radha", "salary": 35000, "department": "spoting", "exp": 3}

]

#print employee names

# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)

#print name in uppercase

# e_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
#
# print(e_upper)
