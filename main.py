from turtle import Screen
from slider import Slider
from ball import Ball
from board import ScoreBoard
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)


right_bar = Slider(x_position=370)
left_bar = Slider(x_position=-380)
ball = Ball()

pong_board = ScoreBoard()
pong_board.update_board()

my_screen.listen()
my_screen.onkey(ball.move, "Return")
my_screen.onkey(right_bar.up, "Up")
my_screen.onkey(right_bar.down, "Down")
my_screen.onkey(left_bar.up, "a")
my_screen.onkey(left_bar.down, "z")


while True:
    time.sleep(0.03)
    my_screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()

    if (ball.xcor() > 355 and ball.distance(right_bar) < 50) or (ball.xcor() < -360 and ball.distance(left_bar) < 50):
        ball.x_bounce()


    if ball.xcor() > 390:
        ball.reset_position()
        pong_board.right_point()

    if ball.xcor() < -390:
        ball.reset_position()
        pong_board.left_point()

#my_screen.exitonclick()
