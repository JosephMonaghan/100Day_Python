from turtle import Turtle
import random

POSSIBLE_COORDINATES=range(-280,280,20)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.pu()
        self.speed('fastest')
        rd_coords=[random.choice(POSSIBLE_COORDINATES), random.choice(POSSIBLE_COORDINATES)]
        self.setpos(rd_coords)

    def am_i_eaten(self,headpos):
        if self.pos() == headpos:
            rd_coords=[random.choice(POSSIBLE_COORDINATES), random.choice(POSSIBLE_COORDINATES)]
            self.setpos(rd_coords)
            return True




