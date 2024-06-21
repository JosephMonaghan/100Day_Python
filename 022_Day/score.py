from turtle import Turtle
FONT_SIZE=50
ALIGNMENT="center"
FONT='courier'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 220)
        self.left_score=0
        self.right_score=0
        self.color("white")
        self.score_board()
        self.pu()
        self.hideturtle()
    
    def someone_scored(self, ball_pos):
        if ball_pos < 0:
            self.message="Right Scored! Space to keep playing"
            self.right_score+=1
        else:
            self.message="Left Scored! Space to keep playing"
            self.left_score+=1
        
        self.clear()
        self.goto(0, 0)
        self.write(self.message,align=ALIGNMENT,font=(FONT, 25, 'bold'))

    def score_board(self):
        self.goto(0, 220)
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}",align=ALIGNMENT,font=(FONT, FONT_SIZE, 'bold'))
