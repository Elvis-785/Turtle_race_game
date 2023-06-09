from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Choose color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-200, -150, -100, 0, 100, 200]

all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on_race = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_on_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
