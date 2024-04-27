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
    cursor.backward(10)

def clear_screen():
    screen.clearscreen()
    cursor.home()