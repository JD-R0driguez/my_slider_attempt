from turtle import Turtle
from ball import Ball
from slider import Slider

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_board(self):
        self.clear()
        self.goto(-180, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
        self.goto(180, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))

    def right_point(self):
        self.right_score += 1
        self.update_board()

    def left_point(self):
        self.left_score += 1
        self.update_board()