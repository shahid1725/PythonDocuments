#DECORATORS
#-----------

# def div(num1,num2):
#     return num1/num2
# print(div(3,6))   #IF IN THIS CASE RESULT WILL BE FRACTION ..SO WE USE DECORATORS TO SWAP NUMBERS TO GET GREAT NUMBER IN FIRST ORDER

def revert_val(func):   #division(3,6)
    def wrapper(num1,num2):          #NO.OF VAROUBLES SAME AAKANAM
        if num1<num2:
            (num1,num2)=(num2,num1)  #swapping -- division(6,3)
            return func(num1,num2)
        else:
            return func(num1,num2)
    return wrapper

@revert_val
def division(num1,num2):
    return num1/num2
print(division(3,6))

# @revert_val                 #ORU DECERATOR KOND ETHRA FUNCTIONUM WORK CHEYYUM
# def substract(num1,num2):
#     return num1-num2
# print(substract(2,10))


#USER ACCOUNT DELETION AND CHANGE PIN
#------------------------------------

# def admin_required(func):
#     def wrapper(a,b):
#         if a!="admin":
#             raise Exception("YOU ARE NOT ALLOWED")
#         else:
#             return func(a,b)
#     return  wrapper
#
# @admin_required
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
#
# @admin_required
# def deleteac(user,accno):
#     return str(accno)+"delete"
#
# print(change_pin("admin",1000))         #if we place name other than admin exception will raise
# print(deleteac("admin",12300))


#Q..ASK USER FOR VACCINATION...IF USER BELOW 18 NOT ELIGIBLE FOR VACCINATION

# def vaccine(func):
#     def detials(a,b,c):
#         if b<18:
#             raise Exception("YOU ARE NOT ELIGIBLE FOR VACCINATION")
#         else:
#             return func(a,b,c)
#     return detials
#
# @vaccine
# def user_det(name,age,place):
#     return "ELIGIBLE"
#
# # print(user_det("SHYAM",17,"CHEMMAD"))
# print(user_det("SUSHIN",26,"CALICUT"))