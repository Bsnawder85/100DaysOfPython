from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
is_race_on = False

# 4 turtles in the race
leonardo = Turtle(shape="turtle")
raphael = Turtle(shape="turtle")
michelangelo = Turtle(shape="turtle")
donatello = Turtle(shape="turtle")

leonardo.color("blue")
raphael.color("red")
michelangelo.color("orange")
donatello.color("purple")

all_turtles = [leonardo, raphael, michelangelo, donatello]

for turtle in all_turtles:
    turtle.penup()

leonardo.goto(x=-230, y=75)
raphael.goto(x=-230, y=25)
michelangelo.goto(x=-230, y=-25)
donatello.goto(x=-230, y=-75)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {user_bet} turtle won.")
                is_race_on = False
                break
            else:
                print(f"You lost! The {winning_color} turtle won.")
                is_race_on = False
                break

        rand_distance = random.randint(0, 10)  # how far each turtle moves per loop, at varying speed.
        turtle.forward(rand_distance)

screen.exitonclick()
