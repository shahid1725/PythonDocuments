employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id": 1001, "e_name": "joju", "salary": 20000, "department": "operating", "exp": 1},
    {"e_id": 1002, "e_name": "raju", "salary": 15000, "department": "experting", "exp": 0},
    {"e_id": 1003, "e_name": "ramu", "salary": 11000, "department": "marketing", "exp": 2},
    {"e_id": 1004, "e_name": "radha", "salary": 35000, "department": "spoting", "exp": 3}

]

#1)print amployee names only

# for employee in employees:
#     print(employee["e_name"])

#print emplyee names in uppercase

# for employee in employees:
#     print(employee["e_name"].upper())

#2)print employee name working as marketing

# for employee in employees:
#     if (employee["department"]=="marketing"):    #condition
#         print(employee["e_name"])

#3)total sum of salary
# sum=0
# for employee in employees:
#
#     sum+=employee["salary"]
# print(sum)


#here first 3 case , in 1 we have direct outputs so called MAPPING
#in 2nd case we have to apply some conditions , so called FILTERING
#in 3rd case we have to process and to get into single value  ,so called REDUCE



#print employee names starting with "r" (FILTERING)
#print employee highest salary (REDUCE)
#print lowest salary (SALARY)
#add bonus to all employees (MAPPING)
#add bonus 5000 to marketing (FILTERING)

