from turtle import Turtle, Screen
import time

INITIAL_LENGTH=3
INITIAL_X=0
INITIAL_Y=0
INITIAL_TRAJECTORY="west"
trajectory=INITIAL_TRAJECTORY

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(False)
screen.listen()


my_snake=[]
def start_up():
    '''Draws the initial snake at the center position, with tail going to the left'''
    global INITIAL_LENGTH, INITIAL_X, INITIAL_Y
    for i in range(INITIAL_LENGTH):
        new_seg=Turtle(visible=False)
        new_seg.speed(0)
        new_seg.pu()
        new_seg.setpos(INITIAL_X - i*20,INITIAL_Y)
        new_seg.shape('square')
        new_seg.color('white')
        new_seg.speed(5)
        new_seg.showturtle()
        my_snake.append(new_seg)
        screen.update()

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

start_up()
snake_length=INITIAL_LENGTH
trajectory="west"

screen.onkeypress(key="w",fun=go_north)
screen.onkeypress(key="a",fun=go_east)
screen.onkeypress(key="s",fun=go_south)
screen.onkeypress(key="d",fun=go_west)

game_is_on=True
while game_is_on:
    replace_pos=my_snake[0].pos()
    my_snake[0].forward(20)
    for seg in range(1,len(my_snake)):
        tmp=my_snake[seg].pos()
        my_snake[seg].setpos(replace_pos)
        replace_pos=tmp
    time.sleep(0.1)
    screen.update()
    




screen.exitonclick()