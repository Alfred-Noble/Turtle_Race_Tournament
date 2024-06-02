# Turtle_Race_Tournament
It is a exclusive python code which offers user to select one of 7 colored turtles, later they are raced which is all autonomous and the winner is declared. It is Fun to play.

# Turtle Race and Key Control Projects Description
## Overview
This repository contains two engaging Python projects using the Turtle graphics module: a Turtle Race game (`multiple_t_race.py`) and a Key-Controlled Turtle drawing program (`keymain.py`). Both projects showcase interactive and dynamic uses of the Turtle module, highlighting different aspects of turtle graphics and user input handling in Python.

##-> Turtle Race Game (`multiple_t_race.py`)

# *Description*
The Turtle Race game allows users to bet on a turtle in a colorful race across the screen. The game involves multiple turtles of different colors racing from the left to the right side of the screen. The first turtle to cross the finish line wins, and the program announces whether the user’s bet was correct.

# *Features*
- **User Interaction:** Prompts the user to place a bet on a turtle before the race starts.
- **Dynamic Racing:** Turtles move forward randomly, making each race unpredictable and exciting.
- **Winning Announcement:** Informs the user if their chosen turtle won or lost the race.

# *User-Defined Functions*
- No specific user-defined functions were created in this script. The functionality is implemented directly in the main program flow.

# *Library Intrinsic Methods*
- **`turtle.Turtle()`**: Creates a new turtle object.
- **`turtle.Screen()`**: Sets up the screen for the race.
- **`screen.setup(width, height)`**: Configures the screen size.
- **`screen.textinput(title, prompt)`**: Prompts the user to input their bet.
- **`turtle.Turtle().color()`**: Sets the turtle's color.
- **`turtle.Turtle().penup()`**: Lifts the pen so the turtle moves without drawing.
- **`turtle.Turtle().goto(x, y)`**: Moves the turtle to a specified position.
- **`turtle.Turtle().forward(distance)`**: Moves the turtle forward by a specified distance.
- **`turtle.Turtle().xcor()`**: Returns the turtle’s current x-coordinate.
- **`screen.exitonclick()`**: Keeps the screen open until a mouse click.

##-> Key-Controlled Turtle (`keymain.py`)

# *Description*
The Key-Controlled Turtle program allows users to control a turtle's movements on the screen using keyboard keys. The turtle can move forward, backward, rotate left, rotate right, and clear the drawing area, making it a fun way to create interactive drawings.

# *Features*
- **Keyboard Controls:** Users can move the turtle in different directions using the keys W, S, A, and D.
- **Drawing and Clearing:** Users can draw with the turtle and clear the screen with the C key.
- **Real-time Interaction:** The turtle responds immediately to key presses for a smooth and interactive experience.

# *User-Defined Functions*
- move_forward(): Moves the turtle forward by 10 units.
- move_backward(): Moves the turtle backward by 10 units.
- counter_clockwise(): Rotates the turtle 10 degrees counter-clockwise.
- clockwise(): Rotates the turtle 10 degrees clockwise.
- clearing(): Clears the drawing, moves the turtle back to the starting position, and resets the pen.

# *Library Intrinsic Methods*
- **`turtle.Turtle()`**: Creates a new turtle object.
- **`turtle.Screen()`**: Sets up the screen for interaction.
- **`turtle.Turtle().fd(distance)`**: Moves the turtle forward by a specified distance.
- **`turtle.Turtle().backward(distance)`**: Moves the turtle backward by a specified distance.
- **`turtle.Turtle().heading()`**: Returns the turtle's current heading.
- **`turtle.Turtle().setheading(to_angle)`**: Sets the turtle's heading to a specific angle.
- **`turtle.Turtle().clear()`**: Clears all drawings made by the turtle.
- **`turtle.Turtle().penup()`**: Lifts the pen so the turtle moves without drawing.
- **`turtle.Turtle().home()`**: Moves the turtle to the starting position.
- **`turtle.Turtle().pendown()`**: Lowers the pen to start drawing.
- **`screen.listen()`**: Sets the screen to listen for key presses.
- **`screen.onkey(fun, key)`**: Binds a function to a key press.
- **`screen.exitonclick()`**: Keeps the screen open until a mouse click.

## *Future Enhancements*
- For Turtle Race Game:
  - Add more turtles to the race for increased complexity.
  - Introduce obstacles or power-ups to make the race more exciting.
  - Provide a graphical interface for placing bets.

  For Key-Controlled Turtle:
  - Add more drawing functions such as changing pen color and size.
  - Implement shape-drawing capabilities (e.g., squares, circles) controlled by different keys.
  - Include a way to save the drawings as image files.
