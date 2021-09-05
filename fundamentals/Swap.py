#method 1 using temporary variable

a=5
b=4

temp=a
a=b
b=temp

print("a :" ,a)
print("b :" ,b)

#method 2

a=6
b=1

a,b=b,a

print("a :" ,a)
print("b :" ,b)

#method 3 for common prgm languages

a=1
b=2

a=a+b
b=a-b
a=a-b

print("a :" ,a)
print("b :" ,b)
