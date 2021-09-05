#INHERITANCE
#ORU CLASSINTE PROPERTIES VERE CLASSINUM KODUKKUKA

#-----SINGLE INHERITANCE---------
# class Person:                             #PARENT/BASE/SUPER CLASS
#     def walk(self):
#         print("person is walking")
#     def read(self):
#         print("person is reading")
#
# class Student(Person):                     #CHILD/DERIVED/SUB CLASS
#     def exam(self):
#         print("student attending exam")
#
# pe=Person()
# pe.walk()
# pe.read()
#
# st=Student()
# st.exam()
# st.walk()
# st.read()

#Q...CREATE PERSON CLASS WITH SINGLE INHERITANCE
# class Person:
#     def seting(self,name,age,place,degree):
#         self.name=name
#         self.age=age
#         self.place=place
#         self.degree=degree
#     def printva(self):
#         print("NAME",self.name)
#         print("AGE",self.age)
#         print("PLACE",self.place)
#         print("DEGREE",self.degree)
# class Human(Person):
#     def abc(self,phone,car):
#         self.phone=phone
#         self.car=car
#     def prin(self):
#         print("PHONE",self.phone)
#         print("CAR:",self.car)
#
#
#
# hu=Human()
# hu.abc(965869,"mini cooper")
# hu.prin()
# hu.seting("RAFEEQ",20,"CALICUT","DOCTOR")
# hu.printva()



#VEHICLE CLASS - BUS CLASS
# class Vehicle:
#     def setvalue(self,name,number,model):
#         self.name=name
#         self.number=number
#         self.model=model
#     def printvalue(self):
#         print("Name of the vehicle:",self.name)
#         print("Number of the vehicle :",self.number)
#         print("Model of the vehicle :",self.model)
#
# class Bus(Vehicle):
#     def set(self,colour,route,tyre):
#         self.colour=colour
#         self.route=route
#         self.tyre=tyre
#     def pri(self):
#         print("Colour of the bus:",self.colour)
#         print("Route of the bus :",self.route)
#         print("Tyre of the bus :",self.tyre)
#
# bu=Bus()
# bu.setvalue("ASHOK LEYLAND","KL11AP2032",2013,)
# bu.set("GREEN","KOZHIKODE","NIPPON")
# bu.printvalue()
# bu.pri()


#Q...BOOK CLASS

# class Book:
#     def setvalue(self,library_name,book_name,author,pages):
#         self.library_name=library_name
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#     def printvalue(self):
#         print("Library name :",self.library_name)
#         print("Book name :",self.book_name)
#         print("Author name :",self.author)
#         print("No of Pages :",self.pages)
#
# bo=Book()
# bo.setvalue("APJ LIBRARY OF BOOKS","HALF GIRLFRIEND","CHETAN BAGATH",314)
# bo.printvalue()

#-----MULTIPLE INHERITANCE------------

# class Person:
#     def set(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#         print(self.name,self.age,self.place)
#
# class Child:
#     def setval(self,school,standard):
#         self.school=school
#         self.standard=standard
#         print(self.school,self.standard)
#
# class Student(Person,Child):
#     def suuu(self,rollno,department,mark):
#         self.rollno=rollno
#         self.department=department
#         self.mark=mark
#         print(self.rollno,self.mark,self.department)
#
# st=Student()
# st.set("BABY",12,"CHEMMAD")
# st.setval("st.pauls",5)
# st.suuu(12,520,"Biology")

#Q...MULTIPLE INHERITANCE...PERSON ,PARENT,EMPLOYEE CLASS
#
# class Person:
#     def set(self, name, age, place):
#          self.name=name
#          self.age=age
#          self.place=place
#          print(self.name,self.age,self.place)
# class Parent:
#     def saa(self,phone):
#         self.phone=phone
#         print(self.phone)
# class Employee(Person,Parent):
#     def eee(self,id,salary,position):
#         self.id=id
#         self.salary=salary
#         self.position=position
#         print(self.id,self.salary,self.position)
#
# em=Employee()
# em.set("BEENA",23,"KOCHI")
# em.saa(985623)
# em.eee(12,23000,"MANAGER")


# #Q....CREATE MULTIPLE INHERITANCE PERSON,PARENT,TEACHER..
# class Person:
#     def per(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#         print("NAME:",self.name)
#         print("AGE:",self.age)
#         print("PLACE:",self.place)
# class Parent:
#     def par(self,phone,occupation):
#         self.phone=phone
#         self.occupation=occupation
#         print("PHONE:",self.phone)
#         print("OCCUPATION:",self.occupation)
# class Teacher(Person,Parent):
#     def tea(self,school,subject):
#         self.subject=subject
#         self.school=school
#         print("SCHOOL:",self.school)
#         print("SUBJECT:",self.subject)
#
# te=Teacher()
# te.per("BINDU",28,"CHALAKKUDY")
# te.par(985695,"TEACHER")
# te.tea("ST.JOSEPH","BIOLOGY")

#--------MULTI LEVEL / HIERARCHIAL  INHERITENCE---------

# class A:
#     def AAAAA(self):
#         print("inside A")
# class B(A):
#     def BBBBB(self):
#         print("inside B")
# class C(B):
#     def CCCCC(self):
#         print("inside c")
#
# a=A()
# a.AAAAA()
#
# b=B()
# b.AAAAA()
# b.BBBBB()
#
# c=C()
# c.AAAAA()
# c.BBBBB()
# c.CCCCC()

#Q...PERSON-CHILD-STUDENT USING MULTI LEVEL

# class Person:
#     def p(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child(Person):
#     def c(self,sweets,hero):
#         self.sweets=sweets
#         self.hero=hero
#         print(self.sweets,self.hero)
# class Student(Child):
#     def s(self,school,subject):
#         self.school=school
#         self.subject=subject
#         print(self.school,self.subject)
# #
#
# st=Student()
# st.s("ohss","biology")
# st.c("ladoo","dq")
# st.p("shahid",12)


#Q...PERSON-(CHILD/PARENT)...STUDENT(CHILD)...
# class Person:
#     def ppp(self,name,age):
#         self.name = name
#         self.age=age
#         print(self.name,self.age)
# class


#-------------INHERIT USING CONSTRUCTOR--------------------------------------------------------------------------
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print("name",self.name)
#         print("age",self.age)
# class Student(Person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def printzz(self):
#         print(self.rollno)
#         print(self.mark)
#         print(self.name)
#         print(self.age)
#
# st=Student(2,25,"shahid",15)
# st.printval()
# st.printzz()

#ANIMAL CLASS - DOG CLASS
#------------------------

# class Animal:
#     def __init__(self,name,age,colour):
#         self.name=name
#         self.age=age
#         self.colour=colour
#     def printvalue(self):
#         print("Name of the Animal:",self.name)
#         print("Age of the animal:",self.age)
#         print("Colour of the animal:",self.colour)
#
# class Dog(Animal):
#     def __init__(self,family,breed,name,age,colour):
#         super().__init__(name,age,colour)
#         self.family=family
#         self.breed=breed
#     def pri(self):
#         print("Family :" ,self.family)
#         print("Breed :",self.breed)

#
# do=Dog("CANIDAE","GERMAN SHEPHERD","ARJUN",3,"GOLDEN YELLOW")
# do.printvalue()
# do.pri()

#Q..PERSON-EMPLOYEE
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printopii(self):
#         print("name :",self.name)
#         print("age:",self.age)
#
# class Employee(Person):
#     def __init__(self,salary,department,name,age):
#         super().__init__(name,age)
#         self.salary=salary
#         self.department=department
#     def print(self):
#         print("salary:",self.salary)
#         print("department:",self.department)
#
# em=Employee(20000,"physics","shahid",23)
# em.printopii()
# em.print()


#---------TWO STRING METHOD-------

#Q...VEHICLE CLASS-MODEL,REG.NO,COLOR
# class Vehicle:
#     def __init__(self,model,regno,color):
#         self.model=model
#         self.regno=regno
#         self.color=color
#     def printvalue(self):
#         print("model:",self.model)
#         print("regno:",self.regno)
#         print("color:",self.color)
#     def __str__(self):                  #two string method for common
#         return self.model+self.color
#
# ve=Vehicle("LXI","KL65J3442","BLACK")
# ve.printvalue()
# print(ve)

#Q...STUDENT CLASS-NAME,ROLLNO,DEPT,COLLEGE  ---- common-name,dept
# class Student:
#     college="psmo"
#     def __init__(self,name,rollno,dept):
#         self.name=name
#
#         self.rollno=rollno
#         self.dept=dept
#     def printvalue(self):
#         print(self.name,self.rollno,self.dept,Student.college)
#     def __str__(self):
#         return self.name+str(self.rollno)      #if it is integer , conert to string
#
# st=Student("shahid",12,"physics")
# st.printvalue()
# print(st)


#Q........PARENT CLASS,TEACHER CLASS  ...CONSTRUCTOR,INHERITENCE,TCHR COMMON VALUE - NAME,ID
# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printvalue(self):
#         print(self.name,self.age)
#
# class Teacher(Parent):
#     def __init__(self,subject,id,name,age):
#         super().__init__(name,age)
#         self.subject=subject
#         self.id=id
#     def printo(self):
#         print(self.id,self.subject,self.name,self.age)
#
#     def __str__(self):
#         return str(self.id)+" "+self.name
#
# te=Teacher("maths",1725,"bindu",32)
# te.printo()
# print(te)


#---------------POLYMORPHISM------------------
#1.  OVER LOADING.......same method name and different number of parameters
#2.  OVER RIDING.......same method name and same number of parameters


#OVER LOADING
#-----------    ("now python doesnot support over loading")
# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
# st=Student()
# st.show(3)

#Q....
# class Mango:
#     def fruit(self,color,size):
#         self.color=color
#         self.size=size
#         print(self.size,self.color)
# class Apple(Mango):
#     def fruit(self,smell):
#         self.smell=smell
#         print(self.smell)
# ap=Apple()
# ap.fruit("red",12)

#q....
# class Operators:
#     def num(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
#     def num(self,num3):
#         self.num3=num3
#         print(self.num3)
#
# np=Operators()
# op.num(6,7)                             #CALCULATE THE  NUMBER OF ARGUMENTS

#OVER RIDING
#----------SAME METHOD, SAME NO.OF ARGUMENTS
# class Person:
#     def printval(self,name):
#         self.name=name
#         print("inside person method",self.name)
# class Child(Person):
#     def printval(self,class1):
#         self.class1=class1
#         print("inside child method",self.class1)
#
# ch=Child()
# ch.printval("abc")                       #IVIDE 2ND CLASS WORK CHEYYUM, CHILD CLASS PERSON CLASSINE OVER RIDE CHEYYUM


#Q...
# class Emplyee:
#     def man(self,name):
#         self.name=name
#         print("employee name:",self.name)
# class Teacher(Emplyee):
#     def man(self,school):
#         self.school=school
#         print("teacher's school:",self.school)
#
# te=Teacher()
# te.man("ghss")

#Q

# class Pen:
#     def setvalue(self,name):
#         self.name=name
#         print("Name :",self.name)
#
# class Book(Pen):
#     def set(self,colour):
#         self.colour=colour
#         print("COLOUR :",self.colour)
# bo=Book()
# bo.set("RED")
#-----------------------------------------------------------
#Q...OOP-INHERITENCE -> QUESTION FILE from there import file and create student class

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print("name:",self.name)
#         print("age:",self.age)
#     def __str__(self):
#         return self.name
#
# f1=open("question",'r')
# for line in f1:
#     # print(line)
#     l=line.split(",")
#     # print(l)
#     name=l[0]
#     age=l[1]
#
#     st=Student(name,age)
#     print(st)
#     st.printval()

#Q...CREATE THE OBJECT OF STUDENT FROM question2file
# class Student:
#     def __init__(self,name,no,subject,mark):
#         self.name=name
#         self.no=no
#         self.subject=subject
#         self.mark=mark
#     def printval(self):
#         print("name:",self.name)
#         print("no:",self.no)
#         print("subject:",self.subject)
#         print("mark:",self.mark)
#     def __str__(self):
#         return self.name
# f=open("question2file","r")
# for line in f:
#     # print(line)
#     l=line.split(",")
#     # print(l)
#     name=l[0]
#     no=l[1]
#     subject=[2]
#     mark=int(l[3])
#     st=Student(name,no,subject,mark)
#     print(st)
#     st.printval()


# count={}
# f=open("mm","r")
# for n in f:
#     wr=n.split(" ")
#     # print(wr)
#     for word in wr:
#         if word not in count:
#             count.update({word:1})
#         else:
#             val=int(count[word])
#             val+=1
#             count.update({word:val})
# print(count)


