from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.color("white")

    def go_up(self):
        my_xcor = self.xcor()
        my_ycor = self.ycor()
        self.goto(my_xcor, my_ycor + 20)

    def go_down(self):
        my_xcor = self.xcor()
        my_ycor = self.ycor()
        self.goto(my_xcor, my_ycor - 20)
