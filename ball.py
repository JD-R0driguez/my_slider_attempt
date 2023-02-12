from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_pase = 5
        self.y_pase = 5


    def move(self):

        new_x = self.xcor() + self.x_pase
        new_y = self.ycor() + self.y_pase
        self.goto(new_x, new_y)


    def x_bounce(self):
        self.x_pase *= -1


    def y_bounce(self):
        self.y_pase *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()