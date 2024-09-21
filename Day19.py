import turtle
from turtle import Turtle, Screen
import random
israceon = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?Enter a color:")
colours = ["pink","wheat","dark goldenrod","medium orchid","dark red","medium violet red","green yellow"]
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    israceon=True

while israceon:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            israceon = False
            wincolor = turtle.pencolor()
            if wincolor == user_bet:
                print(f"You won! the {wincolor} turtle is the winner!")
            else:
                print(f"You lose! the {wincolor} turtle has won")

        dist = random.randint(0,10)
        turtle.forward(dist)
screen.exitonclick()