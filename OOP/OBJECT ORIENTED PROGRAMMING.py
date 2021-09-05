#OOP-OBJECT ORIENTED PROGRAMMING
#CLASS.............design pattern
#OBJECT...........real world entity
#REFERENCE........operations

#class
# class Person:
#     def walk(self):    #self---instance keyword
#         print("person is walking")
#     def read(self):
#         print("person is reading")
#
# #object
# pe=Person()
# pe.walk()
# pe.read()
#
# #object2
# pe2=Person()
# pe.walk()
# pe.read()

#Q.CREATE BOOK CLASS
# class Book:
#     def table(self):
#         print("book is on table")
#     def chair(self):
#         print("book is on chair")
# bo=Book()
# bo.table()
# bo.chair()

# class Person:
#     def setvalue(self,name,father,age):
#         self.name=name                  #instance variable
#         self.father=father
#         self.age=age
#     def printvalue(self):
#         print("Name is",self.name,",and father name is",self.father,"their age is",self.age)
# pe=Person()
# pe.setvalue("Dulqer salmaan","Mammmootty",35)
# pe.printvalue()

#Q..CREATE EMPLOYEE CLASS....ID,NAME,SALARY,AGE,COMPANY NAME,DEPARTMENT
# class Employee:
#     def setvalue(self,id,name,salary,age,companyname,department):
#         self.id=id
#         self.name=name
#         self.salary=salary
#         self.age=age
#         self.companyname=companyname
#         self.department=department
#     def printvalue(self):
#         print("ID NUMBER IS:",self.id,"NAME IS :",self.name,"SALARY IS:",self.salary,"AGE IS:",self.age,"COMPANY NAME IS:",self.companyname,"DEPARTMENT IS:",self.department)
#
# em=Employee()
# em.setvalue(123,"FAHAD",45000,35,"GOOGLE","MANAGEMENT")
# em.printvalue()


#Q...ADD TWO NUMBERS
# class Addition:
#     def abcd(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
# ad=Addition()
# ad.abcd(3,5)

#Q...ADD TWO NUMBERS user input
# class Addition:
#     def abcd(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
# ad=Addition()
# num1=int(input("enter first number"))
# num2=int(input("enter secondn number"))
# ad.abcd(num1,num2)

#Q..CREATE STUDENT CLASS- ROLL NO,NAME,CLASS,SCHOOL NAME
# class Student:
#     def setvalue(self,rollno,name,classs,schoolname):
#         self.rollno=rollno
#         self.name=name
#         self.classs=classs
#         self.schoolname=schoolname
#     def printvalue(self):
#         print("ROLL NO",self.rollno,"name is",self.name,"in class of",self.classs,"in",self.schoolname,"school")
# st=Student()
# st.setvalue(12,"boby",5,"ohss tirurangadi")
# st.printvalue()

#instance variable----self vech call cheyyunna variables...related to methods    (self.-----------)

#STATIC VARIABLES---------related to class      (class name.-----------)   set a common for everything

#if in case of school name we dont need to repeat the same thing ...set that as static variable and print the name with class name

# class Student:
#     school="ghss tirurangadi"
#     def setvalue(self,rollno,name,classs):
#         self.rollno=rollno
#         self.name=name
#         self.classs=classs
#
#     def printvalue(self):
#         print("ROLL NO",self.rollno,"name is",self.name,"in class of",self.classs,"in",Student.school,"school")
# st=Student()
# st.setvalue(12,"boby",5)
# st.printvalue()
#
# st2=Student()
# st2.setvalue(13,"jony",8)
# st2.printvalue()


#Q....EMPLOYEE QN WITH STATIC
# class Employee:
#     company="google"
#     def qwert(self,id,name,department,salary,age):
#         self.id=id
#         self.name=name
#         self.salary=salary
#         self.age=age
#         self.department=department
#         print("emplymee id",self.id,"name",self.name,"in",self.department,"department","with",self.salary,"in",self.age,"th age","in",Employee.company,"company")
#
# em=Employee()
# em.qwert(23,"shahid","CEO",963333332,30)
# em=Employee()
# em.qwert(24,"sulaiman","Operator",33332,40)
# em=Employee()
# em.qwert(21,"rashid","Engineer",2000,30)

#Q...CREATE BANK CLASS...ACCOUNT CREATION,DEPOSIT,WITHDRAWEL
# class Bank:
#     def account(self,name,age,place,minbalance):
#         self.name=name
#         self.age=age
#         self.minbalance=minbalance
#         self.place=place
#         self.balance=self.minbalance
#     def deposit(self,depositamount):
#         self.depositamount=depositamount
#         self.balance+=self.depositamount
#         self.totalamount=print("balance:",self.minbalance+self.depositamount)
#
#     def withdrawel(self,money):
#
#         self.money=money
#         if self.money>self.balance:
#             print("insufficient balance")
#
#         else:
#             print("account debited with",self.money,"rupees")
#             self.balance-=self.money
#             print("balance:",self.balance)
#
# ba=Bank()
# ba.account("shahid",26,"chemmad",1000)
# ba.deposit(10000)
# ba.withdrawel(2000)














