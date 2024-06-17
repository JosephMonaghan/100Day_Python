from turtle import Screen
from turtle import Turtle

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong v1")
screen.tracer(0)

right_paddle=Turtle()
right_paddle.speed(10)
right_paddle.color('white')
right_paddle.shape('square')
right_paddle.pu()
right_paddle.resizemode('user')
right_paddle.turtlesize(stretch_wid=5,stretch_len=1)
right_paddle.setpos(x=350, y=0)


def go_up():
    global right_paddle
    cur_pos=right_paddle.pos()
    new_y=cur_pos[1]+20
    right_paddle.goto(cur_pos[0],new_y)

def go_down():
    global right_paddle
    cur_pos=right_paddle.pos()
    new_y=cur_pos[1]-20
    right_paddle.goto(cur_pos[0],new_y)



screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')

game_is_on=True
while game_is_on:
    screen.update()

screen.exitonclick()
