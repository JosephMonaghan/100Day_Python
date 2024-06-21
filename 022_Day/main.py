from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong v1")
screen.tracer(0)

right_paddle=Paddle([350, 0])
left_paddle=Paddle([-350, 0])
active_ball=Ball()



screen.listen()
screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')

print(active_ball.x_cooldown)

game_is_on=True
while game_is_on:
    active_ball.move()
    active_ball.y_check()
    if active_ball.x_cooldown < 1:
        if active_ball.xcor() >= 330 and active_ball.distance(right_paddle) < 50:
            active_ball.bounce_x()
        elif active_ball.xcor() <= -330 and active_ball.distance(left_paddle) < 50:
            active_ball.bounce_x()
    else:
        active_ball.x_cooldown-=1
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
