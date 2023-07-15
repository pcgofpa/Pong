import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

game_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.initial_movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()
