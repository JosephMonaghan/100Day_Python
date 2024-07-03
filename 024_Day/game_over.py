from turtle import Turtle

FONT_SIZE=22
ALIGNMENT="center"
FONT='courier'


class EndGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.ht()


    def game_over(self,scoreboard):
        self.write("GAME OVER",align=ALIGNMENT,font=(FONT,FONT_SIZE,'bold'))
        if scoreboard.score > scoreboard.highscore:
            scoreboard.highscore=scoreboard.score
            scoreboard.score=0
        

    
    
