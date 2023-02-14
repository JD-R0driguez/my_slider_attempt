from turtle import Turtle

Y_POS = 0

class Slider(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(x=x_position, y=Y_POS)

    def up(self):
        # new_y = slider.ycor() + 20
        # slider.goto(slider.xcor(), new_y)
        self.forward(20)

    def down(self):
        # new_y = slider.ycor() - 20
        # slider.goto(slider.xcor(), new_y)
        self.backward(20)


