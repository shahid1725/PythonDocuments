import random
import time
import turtle

delay=0.1
segment=[]




scrn=turtle.Screen()
scrn.setup(500,500)
scrn.bgcolor("dark blue")
scrn.title("apple snake")
scrn.tracer()

head=turtle.Turtle()
head.shape("circle")
head.color("black")
head.goto(0,0)
head.penup()
head.speed(0)
head.direction="down"

food=turtle.Turtle()
food.shape("square")
food.color("red")
food.goto(0,120)
food.speed(0)
food.penup()
food.shapesize(0.3,0.3)

new_segment=turtle.Turtle()
new_segment.color("black")
new_segment.shape("circle")
new_segment.speed(0)
new_segment.penup()
segment.append(new_segment)

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+15)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-15)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-15)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+15)

scrn.listen()
scrn.onkeypress(go_up,"w")
scrn.onkeypress(go_down,"s")
scrn.onkeypress(go_left,"a")
scrn.onkeypress(go_right,"d")

while True:
    scrn.update()
    if head.distance(food)<10:
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        food.goto(x,y)
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)

    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)

    move()

    time.sleep(delay)
scrn.mainloop()