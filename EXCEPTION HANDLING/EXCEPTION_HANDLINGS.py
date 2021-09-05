#
# NUM1=int(input("enter a number:"))  #in this division program there will be an error when dividing with zero so we use try exception method
# NUM2=int(input("enter a number:"))
# result = NUM1 / NUM2
# print(result)



#
# NUM1=int(input("enter a number:"))
# NUM2=int(input("enter a number:"))
# try:
#     result=NUM1/NUM2      #which program is gonna to exception
#     print(result)           #exception undenkilum ilenkilum try block work cheyyum
# except:
#     print("exception occurred")   #except block work only if there any exception


#2..................
#list=[1,2,3,4]   #in this case when user ask to print index 6?
#print(list[5])

# list=[1,2,3,4,5]
# user=int(input("which index is want to print :"))
# try:
#     print(list[user])
# except:
#     print("Index not exist in list")

# a=[1,2,3]
# index=int(input("enter index"))
# try:
#     print(a[index])                             #try,finally- ella casilum work cheyyum
# except:                                         #except-exception varunna case il mathram work cheyyum
#     print("index not in list")
# finally:
#     print("inside finally")

# a=[10,100,1000]
# index=int(input("enter index:"))
# try:
#     print(a[index])
# except:
#     print("index not in list")
# finally:
#     print("inside finally")


# list=[1,2,5,3]
# index=int(input("enter a index"))
# try:
#     print(list[index])
# except Exception as g:
#     print(g.args)
# finally:
#     print("inside")

#zero division case
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# try:
#     print(num1/num2)
#
# except Exception as f:
#     print(f.args)
# finally:
#     print("ivde enthum pokum")


# #exception raising
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# if num2>num1:
#     raise Exception("number 2 is greater")
# else:
#     print(num1/num2)

#Q..ASK USER AGE,RAISE EXCEPTION IF AGE LS THAN 18
# age=int(input("enter your age:"))
# if age<18:
#     raise  Exception("you are not eligible for vaccination")
# else:
#     print("eligible for vaccination")




