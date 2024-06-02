import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(500,450)
user_bet = screen.textinput(title="Turtle Race Game", prompt="Choose the turtle who you bet on :")
print(user_bet)
colors = ["blue", "red", "green", "yellow", "purple", "brown", "violet"]
y_pos = [150, 100, 50, 0, -50, -100, -150]
list_turtle = []

for turtle_index in range(0, 7):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos[turtle_index])
    list_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_turtle:
        if turtle.xcor() > 250-20:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("Congratulations, You won the bet.")
            else:
                print(f"Alas ! You lost the bet. Winner is {winning_turtle} turtle.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# def various_turtle:
#     tommy = t.Turtle(shape="turtle")
#     tommy.color("purple")
#     tommy.penup()
#     tommy.goto(x=-235, y=100)
#
#     Jimmy = t.Turtle(shape="turtle")
#     Jimmy.color("green")
#     Jimmy.penup()
#     Jimmy.goto(x=-235, y=50)
#
#     Jammy = t.Turtle(shape="turtle")
#     Jammy.color("red")
#     Jammy.penup()
#     Jammy.goto(x=-235, y=0)
#
#     Sammy = t.Turtle(shape="turtle")
#     Sammy.color("yellow")
#     Sammy.penup()
#     Sammy.goto(x=-235, y=-50)
#
#     Ronny = t.Turtle(shape="turtle")
#     Ronny.color("brown")
#     Ronny.penup()
#     Ronny.goto(x=-235, y=-100)


screen.exitonclick()