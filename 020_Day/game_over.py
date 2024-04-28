from turtle import Turtle

FONT_SIZE=22
ALIGNMENT="center"
FONT='courier'


class EndGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.ht()


    def game_over(self):
        self.write("GAME OVER",align=ALIGNMENT,font=(FONT,FONT_SIZE,'bold'))

    
    
