import turtle as t
import random

# colormode is very important
t.colormode(255)
color_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
              (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
              (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90),
              (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109),
              (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()


def dot_line(turtle):
    for _ in range(9):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
    turtle.dot(20, random.choice(color_list))


def dot_two_line(turtle):
    dot_line(turtle)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    dot_line(turtle)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(5):
    dot_two_line(tim)

screen = t.Screen()
screen.exitonclick()
