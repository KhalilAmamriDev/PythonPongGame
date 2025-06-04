import turtle

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
while True:
    wind.update()  # Update the screen
    


    

    





