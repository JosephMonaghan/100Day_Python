from turtle import Turtle
import time

FONT_SIZE=22
ALIGNMENT="center"
FONT='courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 250)
        self.get_highscore()
        self.score=0
        self.ht()
        self.pu()
        self.color("white")
        self.write_score()
        
        
    def get_highscore(self):
        with open('data.txt') as file:
            self.highscore=int(file.read())
    
    def write_highscore(self):
        with open('data.txt',mode='w') as file:
            file.write(str(self.highscore))
    
    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}",align=ALIGNMENT,font=(FONT, 22, 'bold'))

    
    def game_over(self):
        if self.highscore < self.score:
            self.setpos(0,0)
            self.clear()
            self.write("New High Score!",align=ALIGNMENT,font=(FONT, 22, 'bold'))
            self.highscore=self.score
            self.score=0
            #time.sleep(3)
            self.write_highscore()
            self.setpos(0,250)
        self.write_score()
        self.setpos(0, 250)