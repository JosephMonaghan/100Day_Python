from turtle import Turtle, Screen

INITIAL_LENGTH=3
INITIAL_X=0
INITIAL_Y=0

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")

my_snake=[]
def start_up():
    '''Draws the initial snake at the center position, with tail going to the left'''
    global INITIAL_LENGTH, INITIAL_X, INITIAL_Y
    for i in range(INITIAL_LENGTH):
        my_snake.append(Turtle(visible=False))
        my_snake[i].speed(0)
        my_snake[i].pu()
        my_snake[i].setpos(INITIAL_X - i*20,INITIAL_Y)
        my_snake[i].shape('square')
        my_snake[i].color('white')
        my_snake[i].speed('fast')
        my_snake[i].showturtle()

start_up()

screen.exitonclick()