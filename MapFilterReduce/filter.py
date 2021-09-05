# F I L T E R

lst=[1,2,3,4,5,6]
#even numbers

# def check_even(num):
#     return num%2==0

# evens=list(filter(check_even,lst))
# print(evens)


#in lambda form

# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)

# odd=list(filter(lambda num:num%2!=0,lst))
# print(odd)

employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id": 1001, "e_name": "joju", "salary": 20000, "department": "operating", "exp": 1},
    {"e_id": 1002, "e_name": "raju", "salary": 15000, "department": "experting", "exp": 0},
    {"e_id": 1003, "e_name": "ramu", "salary": 11000, "department": "marketing", "exp": 2},
    {"e_id": 1004, "e_name": "radha", "salary": 35000, "department": "spoting", "exp": 3}

]


#FIND EMPLOYEE WHO HAS MARKETING FIELD


marketing=list(filter(lambda emp:emp["department"]=="marketing",employees))
# print(marketing)
marketing_name=list(map(lambda mark:mark["e_name"],marketing))
print(marketing_name)