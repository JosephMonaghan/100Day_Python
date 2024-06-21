from turtle import Turtle

class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.width(5)
        self.hideturtle()

    def draw_board(self):    
        self.pu()
        self.goto(0, 300)
        self.setheading(270)
        for i in range(int(600/50)):
            self.pd()
            self.forward(25)
            self.pu()
            self.forward(25)
    
    def someone_scored(self):
        self.clear()