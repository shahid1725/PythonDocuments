# fibanocci series
# elements will be the sum of previous two numbers
# 0,1,1,2,3,5,8,13..........

#
# first 10 numbers fib numbers
n1=0
n2=1
for i in range(10):
    print(n1)  #.........print....n1=0,1,1
    nth=n1+n2  #nth=1,2,3
    n1=n2      #n1=1,1,2
    n2=nth     #n2=1,2,3

