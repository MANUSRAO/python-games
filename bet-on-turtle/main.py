from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "purple"]
all_turtles = []
y_position = [-100, -70, -40, -10, 20]
for n in range(0, 5):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[n])
    timmy.goto(x=-230, y=y_position[n])
    all_turtles.append(timmy)
user_guess = screen.textinput(title="Make A Guess", prompt="Which turtle do you think will win the race?").lower()
if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() == 230:
            is_race_on = False
            winner = turtle
            color_win = winner.color()[0]
            if user_guess == color_win:
                print(f"Your {color_win} turtle won the race!!")
            else:
                print(f"{color_win} won the race!!Your {user_guess} turtle lost!!")

screen.exitonclick()

