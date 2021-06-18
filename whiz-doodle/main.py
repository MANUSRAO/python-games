from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_left():
    tim.left(30)


def move_right():
    tim.right(30)


def move_backwards():
    tim.back(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key='c', fun=clear)
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=move_right)
screen.exitonclick()
