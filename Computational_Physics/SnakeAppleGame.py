import turtle
import time
import random

delay=0.1
segments=[]
score=0
high_score=0

scrn=turtle.Screen()
scrn.title("snake apple game")
scrn.bgcolor("black")
scrn.setup(width=600,height=600)
scrn.tracer(0)

#snake head
head=turtle.Turtle()
head.shape("square")
head.color("green")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction="down"

#food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.5,0.5)
food.goto(0,150)

#score board
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0  High score : 0",align="center",font=("courier",20,"normal"))
#saying computer direction key
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

def move():   #calling function to move head of snake
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

#to listen which key is pressing
scrn.listen()
scrn.onkeypress(go_up,"w")
scrn.onkeypress(go_down,"s")
scrn.onkeypress(go_left,"a")
scrn.onkeypress(go_right,"d")

while True:
    scrn.update()
    #game over when touch border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for seg in segments:    #after touching border clear segments
            seg.goto(1000,1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("score : {}  High score : {}".format(score, high_score), align="center",
                  font=("courier", 20, "normal"))

    if head.distance(food)<15:
        x=random.randint(-290,290)
        y=random.randint(-290,270)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #score update
        score += 10
        if score>high_score:
            high_score=score
            pen.clear()
            pen.write("score : {}  High score : {}".format(score,high_score),align="center",font=("courier",20,"normal"))

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()
    #when touching body - game over
    for seg in segments:
        if seg.distance(head)<15:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for seg in segments:
                seg.goto(1000,1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write("score : {}  High score : {}".format(score, high_score), align="center",
                  font=("courier", 20, "normal"))

    time.sleep(delay)
scrn.mainloop()