from turtle import Turtle, Screen

cursor = Turtle()
screen=Screen()

def turn_right():
    cursor.right(10)

def turn_left():
    cursor.left(10)

def fwd():
    cursor.forward(10)

def back():
    cursor.forward(-10)

def clear_screen():
    cursor.reset()

screen.listen()
screen.onkey(key="w",fun=fwd)
screen.onkey(key="s",fun=back)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear_screen)


screen.exitonclick()