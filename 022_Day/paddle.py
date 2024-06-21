from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.speed(10)
        self.color('white')
        self.shape('square')
        self.pu()
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.setpos(x=pos[0], y=pos[1])
    
    def move_up(self):
        test=self.pos()
        new_y_pos=self.ycor() + 20
        self.setpos(self.xcor(), new_y_pos)

    def move_down(self):
        new_y_pos=self.ycor() - 20
        self.setpos(self.xcor(), new_y_pos)
    