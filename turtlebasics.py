from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")

colours=["pink","wheat","dark goldenrod","medium orchid","dark red","medium violet red","green yellow"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(50)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


















screen = Screen()
screen.exitonclick()


