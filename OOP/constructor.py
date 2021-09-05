#constructor used to initialise instance variables


# class Person:
#     def __init__(self,name,age,place):   #constructor
#         self.name=name
#         self.age=age
#         self.place=place
#     def printvalue(self):
#         print(self.name,self.age,self.place)
#
# pe=Person("shahid",22,"chemmad")
# pe.printvalue()

#Q...CALCULATOR PROGRAMME USING CONSTRUCTOR


# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def printvalue(self):
#         choice=int(input("select operation:\n1.addition\n2.substraction\n3.multiplication\n4.division"))
#         if choice>4:
#             print("invalid choice")
#         elif choice==1:
#             res=self.num1+self.num2
#             print("result is:",res)
#         elif choice==2:
#             res = self.num1 - self.num2
#             print("result is:", res)
#         elif choice==3:
#             res = self.num1 * self.num2
#             print("result is:", res)
#         elif choice==4:
#             res = self.num1 / self.num2
#             print("result is:", res)
# num1=float(input("enter number :"))
# num2=float(input("enter second number:"))
# ca=Calculator(num1,num2)
# ca.printvalue()

#or

# class Calculator:
#      def __init__(self,num1,num2):
#          self.num1=num1
#          self.num2=num2
#      def add(self):
#             return self.num1+self.num2
#
#      def sub(self):
#              return self.num1 - self.num2
#
#      def mult(self):
#             return self.num1 * self.num2
#
#      def divi(self):
#             return self.num1 / self.num2
#
# num1=float(input("enter number :"))
# num2=float(input("enter second number:"))
# ca=Calculator(num1,num2)
# print(ca.add())
# print(ca.sub())
# print(ca.mult())
# print(ca.divi())

#Q...CREATE TEACHER CLASS....tchr name,department,tchr id,college name

# class Teacher:
#     college_name="PSMO COLLEGE"
#     def __init__(self,name,department,subject,id):
#         self.name=name
#         self.department=department
#         self.subject=subject
#         self.id=id
#     def printvalue(self):
#         print("TEACHER NAME :",self.name)
#         print("SUBJECT:",self.subject)
#         print("DEPARTMENT:",self.department)
#         print("ID:",self.id)
#         print("COLLEGE:",Teacher.college_name)
#
# te=Teacher("shani","science","zoology",236)
# te.printvalue()
#
# te1=Teacher("usman","maths","calculus",123)
# te1.printvalue()

