import turtle
import time  # Add this at the top

wind = turtle.Screen()
wind.title("Ping Pong By Khalil")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # Turns off the screen updates for better performance
# Paddle A
 # madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=5, stretch_len=1)
# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)
    # ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Lower speed
ball.dy = -1  # Ball speed in y direction

# Score variables
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# functions
def madrab1_up():
        y = madrab1.ycor()
        y += 20
        madrab1.sety(y)
def madrab1_down():
        y = madrab1.ycor()
        y -= 20
        madrab1.sety(y)
def madrab2_up():
        y = madrab2.ycor()
        y += 20
        madrab2.sety(y)
def madrab2_down():
        y = madrab2.ycor()
        y -= 20
        madrab2.sety(y)
    #keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# main game loop
try:
    while True:
        wind.update()  # Update the screen
        time.sleep(0.01)  # Add a small delay
        ball.setx(ball.xcor() + ball.dx)  # Move the ball in x direction
        ball.sety(ball.ycor() + ball.dy)  # Move the ball in y direction
        
        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # Reverse the y direction
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
            
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

        if (340 < ball.xcor() < 350) and (madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1
        if (-350 < ball.xcor() < -340) and (madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1
except Exception:
    print("Game closed.")













