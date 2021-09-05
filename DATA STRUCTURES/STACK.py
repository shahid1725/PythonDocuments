#LIFO- LAST IN FIRST OUT
#PUSH-ADD ELEMENT
#POP-REMOVE ELEMENT(from last)
#DISPLAY
#SIZE-Of stack


stck=[]
size=int(input("enter the size :"))
top=0
n=0

def push():
    global top,size
    if(top>size):
        print("stack is full")
    else:
        p=int(input("enter the element want to push:"))
        stck.append(p)
        top+=1
def pop():
    global top,size
    if (top<=0):
        print("stack is empty")
    else:
        stck.pop()
        top-=1
def display():
    print(stck)


while (n!=1):
    print("enter the opeartion want to perform")
    opt=print("press\n1)push\n2)pop\n3)display")
    if (opt==1):
        push()
    elif (opt==2):
        pop()
    elif (opt==3):
        display()
    else:
        print("invalid option")
    n=int(input("do you want to continue press 1 for exit"))