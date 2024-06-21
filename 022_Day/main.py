from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from center_line import CenterLine

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong v1")
screen.tracer(0)
center_line=CenterLine()
center_line.draw_board()


def play_again():
    global ball_in_play
    if ball_in_play is False:
        score.score_board()
        center_line.draw_board()
        active_ball.reset_ball()
        ball_in_play=True



right_paddle=Paddle([350, 0])
left_paddle=Paddle([-350, 0])
active_ball=Ball()
score=Score()

screen.listen()
screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')

game_is_on=True
ball_in_play=True
while game_is_on:
    while ball_in_play:
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

        wait_time=0.1
        for _ in range(active_ball.rally):
            wait_time/=1.1
        
        time.sleep(wait_time)

        if abs(active_ball.xcor()) > 400:
            ball_in_play=False
            center_line.someone_scored()
            score.someone_scored(active_ball.xcor())
            play_again()



    

screen.exitonclick()
