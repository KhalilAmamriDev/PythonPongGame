import turtle

wind = turtle.Screen()
wind.title("Ping Pong By Khalil")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # Turns off the screen updates for better performance
# Paddle A

# main game loop
while True:
    wind.update()  # Update the screen
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
    



 

