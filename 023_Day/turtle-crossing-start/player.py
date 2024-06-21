from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('turtle')
        self.color('red')
        self.setheading(90)
        self.start_pos()
        self.level=1
    
    def start_pos(self):
        self.setpos(STARTING_POSITION)

    def jump_fwd(self):
        self.forward(MOVE_DISTANCE)
    
    def check_pos(self,scoreboard,car_manager):
        if self.ycor() >= FINISH_LINE_Y:
            self.level+=1
            scoreboard.level+=1
            scoreboard.draw_score()
            self.start_pos()
            car_manager.level_up()
            

