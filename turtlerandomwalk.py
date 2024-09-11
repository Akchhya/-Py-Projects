import random
from turtle import Turtle
tim = Turtle()
tim.shape("turtle")

colours=["pink","wheat","dark goldenrod","medium orchid","dark red","medium violet red","green yellow"]
directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
