from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_over import EndGame

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
food = Food()
scoreboard = Scoreboard()
game_over= EndGame()

screen.update()
screen.listen()
screen.onkeypress(key="Up",fun=snake.up)
screen.onkeypress(key="Left",fun=snake.left)
screen.onkeypress(key="Down",fun=snake.down)
screen.onkeypress(key="Right",fun=snake.right)

game_is_on=True
while game_is_on:
    snake.move()
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        scoreboard.score+=1
        scoreboard.write_score()
    
    if snake.out_of_bounds():
        game_is_on=False
        game_over.game_over()

    ##Check for intra-snake collisions
    for segment in snake.seg_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            game_over.game_over()

    time.sleep(0.1)
    screen.update()
    




screen.exitonclick()