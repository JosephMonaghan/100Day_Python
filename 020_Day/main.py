from turtle import Turtle, Screen

INITIAL_LENGTH=3
INITIAL_X=0
INITIAL_Y=0
INITIAL_TRAJECTORY="west"
trajectory=INITIAL_TRAJECTORY

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")

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
        new_seg.speed('fast')
        new_seg.showturtle()
        my_snake.append(new_seg)

def go_north():
    global trajectory
    trajectory='north'

def go_south():
    global trajectory
    trajectory='south'

def go_west():
    global trajectory
    trajectory='west'

def go_east():
    global trajectory
    trajectory='east'

start_up()
snake_length=INITIAL_LENGTH
trajectory="west"

game_is_on=True
while game_is_on:
    new_seg=Turtle(shape='square',visible=False)
    new_seg.speed(0)
    new_seg.pu()
    new_seg.color('white')
    head_pos=my_snake[0].pos()
    if trajectory == "west":
        new_seg.setpos(head_pos[0] + 20,head_pos[1])
    elif trajectory == "east":
        new_seg.setpos(head_pos[0] - 20, head_pos[1])
    elif trajectory == "north":
        new_seg.setpos(head_pos[0], head_pos[1]+20)
    elif trajectory == "south":
        new_seg.setpos(head_pos[0], head_pos[1]-20)
    
    new_seg.showturtle()
    my_snake.insert(0,new_seg)
    while len(my_snake) > snake_length:
        my_snake.pop(-1)











screen.exitonclick()