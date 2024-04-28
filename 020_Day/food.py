from turtle import Turtle
import random

POSSIBLE_COORDINATES=range(-260,260,20)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.pu()
        #self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed('fastest')
        rd_coords=[random.choice(POSSIBLE_COORDINATES), random.choice(POSSIBLE_COORDINATES)]
        self.setpos(rd_coords)

    def relocate(self):
        rd_coords=[random.choice(POSSIBLE_COORDINATES), random.choice(POSSIBLE_COORDINATES)]
        self.setpos(rd_coords)
        self.setheading(random.randint(0,360))





