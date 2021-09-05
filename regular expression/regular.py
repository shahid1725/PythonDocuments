#re--package for pattern matching

# import re
#
# count=0
# matcher=re.finditer ("ab","abaababaab")
# for match in matcher:
#     count+=1
# print("count :",count)


# import re
# count=0
# matcher=re.finditer('ab', 'abaababaab')
# for match in matcher:
#     print("match availabale at",match.start())
#     print("group:",match.group())
#     count+=1
# print("count:",count)


#RULES
#---------------
# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' Ato Z
# x='[a-zA-Z]' BOTH LOWER AND UPPER CASES ARE CHECKED
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words except special characters
# x='\W' for special characters




#QUANTIFIERS
#-----------
# x='a+' a including group
# x='a+' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a




# import re
#
# x='[abc]'  #either a or b or c
# matcher=re.finditer(x,'achsombatbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='[ABC]'
# matcher=re.finditer(x,"ABGTHBCA")
# for ok in matcher:
#     print(ok.start())
#     print(ok.group())


# import re
# x='[^abc]'
# matcher=re.finditer(x,"abgth@#52ac bcsfa")
# for j in matcher:
#     print(j.start())
#     print(j.group())

# import re
# x='[a-z]'   #all small letters
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[A-Z]'   #all capital letters
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[^a-zA-Z]'   #except all letters
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[0-9]'   #all numbers
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[a-zA-Z]'   # all letters
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[^0-9a-zA-Z]'   #except all letters and numbers
# matcher=re.finditer(x,'abhstyAFTHHjkfui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[\w]'   #words
# matcher=re.finditer(x,'abhs tyAFTHHjkf ui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[\W]'
# matcher=re.finditer(x,'abhs tyAFTHHjkf ui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[\d]'
# matcher=re.finditer(x,'abhs tyAFTHHjkf ui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

# import re
# x='[\D]'   #EXCEPT DIGITS
# matcher=re.finditer(x,'abhs tyAFTHHjkf ui7674@#')
# for k in matcher:
#     print(k.start())
#     print(k.group())

#-------------------------------------------------------
#example for quantifiers
#-----------------------

# import re
#
# x="a+"   #a including group...........minimum oru a undenkile consider cheyyullu
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x="a*"   #count including  zero number of a.........a positionil illenkilum check cheyyum
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x="a?"   #count a as each including zero number of a...........a ne seperate aayitt con sider cheyyum
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x="a{2}"   #no of position
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x="a{1,3}"   #minimum 1 a , maximum 3a
# r="aaa abc aaaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x="^a"   #check starting with a
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x="a$"   #check ending a
# r="aaa abc aaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#..........VALIDATION...........

# import re
#
# n="hello"
# x='[a-z]+'   # + means group , or "/w+"      here checking n is valid in x
# matcher=re.fullmatch(x,n)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")


#Q....CHECK VALID
# import re
#
# n="56kg"
# x="[0-9]{2}[a-z]{2}"  #or [0-9]{2}[k][g]
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#Q..PHONE NUMBER VALIDATION
# import re
#
# user=input("enter a number:")
# x='[0-9]{10}'  # or x='\d{10}'
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#Q....VALIDATE ONLY OINDIAN NUMBERS...
# import re
#
# num=input("enter number:")
# x='[+][9][1]\d{10}'        or x='[+][9][1]\d{10}$'   dollar to mean last digit to stop
# match=re.fullmatch(x,num)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#Q...VEHICLE REGISTRATION NUMBER...
# import  re
#
# num=input("vehicle number :")
# x='[K][L]\d{2}[A-Z]{1,2}\d{1,4}$'
# match=re.fullmatch(x,num)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#Q.......MAKE RULE

#.upp,low,end with number - Abc6
# import re
#
# num="Abc6"
# x='[a-zA-Z]+\d$'
# match=re.fullmatch(x,num)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


#Q.......MAIL VALIDATION......

# import re
# user=input("enter your mail id :")
# x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}'    #   + means -------onnenkilum varanam
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#.........starting with a , ending with b............

# import re
# user=input("enter text :")
# x='^a[a-zA-Z0-9\W]*b$'                #here * --- for varaam varaathirikkam
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#Q....MIN LENGTH -8,MAX LENGTH-15 , EXCEPT NUMBERS
# import re
# user=input("enter text :")
# x='([\D]{8,15})'
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#Q......START WITH UPP LETTER,THEN NUMBER,LOWERS,SYMBOLS

# import re
# user=input("enter text :")
# x='^[A-Z]{1}[a-z0-9\W]*'
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
# user=input("enter text :")
# x="\w[A-Z]$"
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#Q......FROM THE FILE "file" print the valid phone numbers

# import re
# f=open("file","r")
# x="[+][9][1]\d{10}$"
# for i in f:
#     # # print(i)
#     # number=i.rstrip("\n")    #striping not mandatory here
#     # # print(number)
#     matcher=re.fullmatch(x,i)
#     if matcher!=None:
#         print(i)

# import re
# f=open("file","r")
# x="[+][9][1]\d{10}$"
# for i in f:
#     matcher=re.fullmatch(x,i)
#     if matcher!=None:
#         print(i)


#Q......from file "verefile" import only python students
#eg:LUM11PY679
# import re
# f2=open("verefile","w")
# x="([L][U][M]\d{2}[P]\d{3}$)"
# f=open("verefile","r")
# for i in f:
#     number=i.rstrip("\n")
#     matcher=re.fullmatch(x,number)
#     if matcher!=None:
#         f2.write(number)
#         f2.write("\n")

#Q. start with a followeed by number end with b
#--------------------
# import re
# user=input("enter text:" )
# x="^[a]\d[b]$"
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#sequence of upp , low
#----------------------
# import re
# user=input("enter text:" )
# x="[A-Z]{1}[a-z]{1}"
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#q...start end with upp,except special char,min5 max 10
#---------------------------------------
# import re
# user=input("enter text:" )
# x="^[A-Z]\w{5,10}[A-Z]$"
# match=re.fullmatch(x,user)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
