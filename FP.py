import os
import turtle
#create a window for the game

#Use the turtle module to get the bars and ball and the pen directions 
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("pink")
win.setup(width=800, height=600)
win.tracer(0) # this turns off the screen updates

#initialize the scores to zero
score_one = 0
score_two = 0

#paddle1 (Player One)
paddle_one = turtle.Turtle()
paddle_one.speed(0) #max speed
paddle_one.shape("square")
paddle_one.color("blue")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0) #Initial position

#paddle2 (Player Two)
paddle_two= turtle.Turtle()
paddle_two.speed(0) #max speed
paddle_two.shape("square")
paddle_two.color("blue")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0) #Initial position on other end 

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0) #Initial position
ball.dx = 2 #Movement in x direction
ball.dy = 2 #Movement in y direction

#pen for writing the scores for both players
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font=("Courier", 24, "normal"))

#Functions for the paddles to move
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

#keyboard bindings to control the paddles
#Player One will use W and S and Player Two will use Up and Down
win.listen()
win.onkeypress(paddle_one_up, "w")
win.onkeypress(paddle_one_down, "s")
win.onkeypress(paddle_two_up, "Up")
win.onkeypress(paddle_two_down, "Down")


#main game loop
while True:
    win.update() #Updates the screen

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checking the border
    #Check for collision with the top border
    #Top and Bottom
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1 #Reverses the y direction

    #Check for collision with bottom border
    elif ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1 #Reverses the y direction
      
    #Check for collision with the right border (Player One Scores)
    #Left and right
    if ball.xcor() > 350:
       score_one += 1
       pen.clear()
       pen.write("Player A: {} Player B: {}".formate(score_one, score_two), align="center", 
                 font=("Courier", 24, "normal"))
       ball.goto(0,0) #Resets the ball position
       ball.dx *= -1 #Reverses the direction

    #Check for collision with the left border (Player Two Scores)
    elif ball.xcor() < -350:
       score_two += 1
       pen.clear()
       pen.write("Player A: {} Player B: {}".formate(score_one, score_two), align="center", 
                 font=("Courier", 24, "normal"))
       ball.goto(0,0) #Resets the ball position
       ball.dx *= -1 #Reverses the direction

    #paddle and ball collision (Player One's paddle)
    if ball.xcor() < -340 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1 #reverses the x direction
        
    #paddle and ball collision (Player Two's paddle)
    elif ball.xcor() > 340 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1 #reverses the x direction 
        



        

