def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2


print("select operation")
print("1.ADD\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.ADDITION\n")

while True:
    choice=int(input("enter the choice :"))
    num1=float(input("enter a number :"))
    num2=float(input("enter a number :"))
    if choice==1:

        print(add(num1,num2))
    elif choice==2:

         print(substract(num1,num2))
    elif choice==3:

        print(multiplication(num1,num2))
    elif choice==4:

        print(division(num1,num2))
    else:
        print("invalid choice")



