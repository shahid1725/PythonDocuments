employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id": 1001, "e_name": "joju", "salary": 20000, "department": "operating", "exp": 1},
    {"e_id": 1002, "e_name": "raju", "salary": 15000, "department": "experting", "exp": 0},
    {"e_id": 1003, "e_name": "ramu", "salary": 11000, "department": "marketing", "exp": 2},
    {"e_id": 1004, "e_name": "radha", "salary": 35000, "department": "spoting", "exp": 3}

]

#sum of salary

# salary=list(map(lambda sal:sal["salary"],employees))
# # print(salary)
# print(sum(salary))

#highest salary

# salary=list(map(lambda sal:sal["salary"],employees))
# # print(salary)
# print(max(salary))

#minimum salary

# salary=list(map(lambda sal:sal["salary"],employees))
# # print(salary)
# print(min(salary))


#REDUCE
#show sum
# from functools import reduce
# lst=[1,2,3,4,5,6,7]
#
# totalsum=reduce(lambda num1,num2:num1+num2,lst)   #in reduce we need two arguments , so num1 and num2
# print(totalsum)

#Q.... largest number using reduce
# from functools import reduce
# lst=[2,4,5,68,6]
# large=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)    #easy method writen below
# print(large)

#Q...LOWEST NUMBER

# from functools import reduce
# lst=[5,9,6,4,8,2,7]
# lowest=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
# print(lowest)













# short method
#Q....big number
# num1=10
# num2=20
# # if num1>num2:
# #     print(num1)
# # else:
# #     print(num2)
#
# print(num2 if num1>num2 else num2)

#Q...Positive negative
# num=int(input("enter a number:"))
# # if num>0:
# #     print("+ve")
# # else:
# #     print("-ve")
#
# print("+ve" if num>0 else "-ve")