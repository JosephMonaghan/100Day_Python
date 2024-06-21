from turtle import Turtle

FONT = ("Courier", 24, "normal")
HOR_ALIGNMENT='center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-260, 260)
        self.level=1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)
    
    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.write("Game Over!",font=FONT,align=HOR_ALIGNMENT)
        self.goto(0, -50)
        self.write(f"Final Level: {self.level}",font=FONT,align=HOR_ALIGNMENT)


