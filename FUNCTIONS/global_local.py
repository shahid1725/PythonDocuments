x=3

def faa():
    #x=6
    global x
    x+=10
    print("local :",x)

faa()

print("global x:",x)