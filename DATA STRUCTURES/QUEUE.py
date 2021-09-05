#FIFO-FIRST IN FIRST OUT
#INSERTION..........enqueue
#DELETION...........dequeue
#DISPLAY

qu=[]
size=int(input("enter size:"))
front=0
last=0
n=0
def insert():
    global front,last,size,qu
    if last>=size:
        print("queue is full")
    else:
        p=int(input("enter element want to insert:"))
        qu.insert(last,p)
        #insert(position,element)
        last+=1

        for i in range(front,last):
            print(qu[i])
def delete():
    global front,last,size,qu
    if last==front:
        print("queue is empty")
    else:
        front+=1
        for i in range(front,last):
            print(qu[i])

while n!=1:
    print("................nter the operation want to perform........................")
    opt=int(input("press \n1.enqueue\n2.dequeue \n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()


