#take input from user and check positive number from that

min=int(input("enter a number:"))
max=int(input("enter a number:"))
while min<=max:
    if min%2==0:
        print(min)
    min=min+1
