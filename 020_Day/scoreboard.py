from turtle import Turtle

FONT_SIZE=22
ALIGNMENT="center"
FONT='courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 250)
        self.score=0
        self.ht()
        self.color("white")
        self.write_score()

    
    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score}",align=ALIGNMENT,font=(FONT, 22, 'bold'))