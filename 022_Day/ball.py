from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        #self.shapesize(stretch_wid=2,stretch_len=2)
        self.color('White')
        self.pu()
        self.x_speed=10
        self.y_speed=10
        self.rally=0
        self.x_cooldown=0
        
    def move(self):
        new_x=self.xcor()+self.x_speed
        new_y=self.ycor()+self.y_speed
        self.goto(new_x,new_y)

    def y_check(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce_y()
    
    def bounce_y(self):
        self.y_speed *= -1
    
    def bounce_x(self):
        self.rally+=1
        self.x_speed *=-1
        self.x_cooldown=3

    def reset_ball(self):
        self.x_speed*=-1
        self.rally=0
        self.y_speed*=-1
        self.setpos(0,0)





    
