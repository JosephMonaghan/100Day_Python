import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#TODO Get player movement working

#TODO Reset player and add to score when end is reached

#TODO get car class objected created - move across screen right to left

#TODO Get car manager to place cars randomly to stop the turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()

screen.listen('on')
screen.onkey(player.jump_fwd,'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    player.check_pos(scoreboard,car_manager)
    car_manager.move_the_cars()
    is_collided=car_manager.check_collisions(player)
    if is_collided:
        game_is_on=False
        scoreboard.game_over()
    screen.update()

screen.exitonclick()