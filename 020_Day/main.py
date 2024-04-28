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





snake = Snake()
screen.update()
screen.listen()
screen.onkeypress(key="Up",fun=snake.up)
screen.onkeypress(key="Left",fun=snake.left)
screen.onkeypress(key="Down",fun=snake.down)
screen.onkeypress(key="Right",fun=snake.right)

game_is_on=True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    screen.update()
    




screen.exitonclick()