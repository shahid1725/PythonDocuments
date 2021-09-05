#grade find

maths=int(input("enter MATHS mark :"))
physics=int(input("enter PHYSICS mark: "))
english=int(input("enter ENGLISH mark :"))
biology=int(input("enter BIOLOGY mark :"))
chemistry=int(input("enter CHEMISTRY mark :"))

total_mark=maths+physics+english+biology+chemistry

if total_mark>=450:
    print("Your Grade is A+")
elif total_mark<=449 and total_mark>=380:
    print("Your Grade is A")
elif total_mark<=379 and total_mark>=300:
    print("Your Grade is b+")
elif total_mark<=299 and total_mark>=200:
    print("Your Grade is B")
elif total_mark<=199 and total_mark>=100:
    print("Your Grade is C+")
elif total_mark<=99 and total_mark>=50:
    print("Your Grade is c")
else:
    print("your grade is D")