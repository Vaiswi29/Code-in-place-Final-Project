import os
import turtle
#create a window
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("pink")
win.setup(width=800, height=600)
win.tracer(0)
#score
score_one = 0
score_two = 0

#paddle1 
paddle_one = turtle.Turtle()
paddle_one.speed(0) #max speed
paddle_one.shape("square")
paddle_one.color("blue")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)
#paddle2
paddle_two= turtle.Turtle()
paddle_two.speed(0) #max speed
paddle_two.shape("square")
paddle_two.color("blue")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", algin = "center", font=("Courier", 24, "normal"))

#Functions
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

#keyboard bindings
win.listen()
win.onkeypress(paddle_one_up, "w")
win.onkeypress(paddle_one_down, "s")
win.onkeypress(paddle_two_up, "Up")
win.onkeypress(paddle_two_down, "Down")


#main game loop
while True:
    win.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checking the border

    #Top and Bottom
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1
       os.system('afplay bounce.wav&')

    elif ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1
       os.system('afplay bounce.wav&')

    #Left and right
    if ball.ycor() > 350:
       score_one += 1
       pen.clear()
       pen.write("Player A: {} Player B: {}".formate(score_one, score_two), align="center", 
                 font=("Courier", 24, "normal"))
       ball.gotto(0,0)
       ball.dy *= -1

    elif ball.ycor() < -350:
       score_two += 1
       pen.clear()
       pen.write("Player A: {} Player B: {}".formate(score_one, score_two), align="center", 
                 font=("Courier", 24, "normal"))
       ball.gotto(0,0)
       ball.dy *= -1

    #paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")



        

