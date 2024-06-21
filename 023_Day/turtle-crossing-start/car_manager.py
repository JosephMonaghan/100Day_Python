from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5



class Car(Turtle):
    def __init__(self,movespeed):
        super().__init__()
        self.pu()
        self.shape('square')
        self.shapesize(stretch_len=1.5,stretch_wid=0.75)
        self.initial_spawn()
        self.setheading=180
        self.move_distance=movespeed
    
    def initial_spawn(self):
        self.goto(random.randint(-150, 300), random.randint(-250, 300))
        self.color(random.choice(COLORS))

    def respawn(self):
        self.goto(300, random.randint(-250, 300))
        self.color(random.choice(COLORS))

    def advance(self):
        self.goto(self.xcor()-self.move_distance,self.ycor())

class CarManager:
    def __init__(self):
        self.car_list=[]
        self.numcars=25
        self.move_distance=STARTING_MOVE_DISTANCE
        for _ in range(self.numcars):
            self.car_list.append(Car(self.move_distance))
    
    def move_the_cars(self):
        for i in range(self.numcars):
            self.car_list[i].advance()
            if self.car_list[i].xcor() < -300:
                self.car_list[i].respawn()
    
    def level_up(self):
        self.move_distance+=MOVE_INCREMENT
        for i in range(self.numcars):
            self.car_list[i].initial_spawn()
            self.car_list[i].move_distance=self.move_distance

    def check_collisions(self,player):
        for i in range(self.numcars):
            dist_x=abs(player.xcor() - self.car_list[i].xcor())
            dist_y=abs(player.ycor() - self.car_list[i].ycor())
            if dist_x < 25 and dist_y < 15:
                return True

    
        




