import turtle
from turtle import Turtle,Screen

screen = Screen()
tim = Turtle()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clearing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W".lower(), fun=move_forward)
screen.onkey(key="S".lower(), fun=move_backward)
screen.onkey(key="A".lower(), fun=counter_clockwise)
screen.onkey(key="D".lower(), fun=clockwise)
screen.onkey(clearing, "C".lower())
screen.exitonclick()
