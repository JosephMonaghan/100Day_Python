from turtle import Turtle, Screen
import time
from snake import Snake

INITIAL_LENGTH=3
INITIAL_X=0
INITIAL_Y=0
INITIAL_TRAJECTORY="west"
trajectory=INITIAL_TRAJECTORY
snake_length=INITIAL_LENGTH

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(False)
screen.listen()

def go_north():
    global trajectory
    trajectory='north'
    my_snake[0].setheading(90)

def go_south():
    global trajectory
    trajectory='south'
    my_snake[0].setheading(270)

def go_west():
    global trajectory
    trajectory='west'
    my_snake[0].setheading(0)

def go_east():
    global trajectory
    trajectory='east'
    my_snake[0].setheading(180)


snake = Snake()
screen.update()

screen.onkeypress(key="w",fun=go_north)
screen.onkeypress(key="a",fun=go_east)
screen.onkeypress(key="s",fun=go_south)
screen.onkeypress(key="d",fun=go_west)

game_is_on=True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    screen.update()
    




screen.exitonclick()