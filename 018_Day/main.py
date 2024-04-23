from turtle import Turtle, Screen
import colorgram
import random

colors = colorgram.extract('hirst.jpg',10)

col_matrix=[]
for i in range(10):
    tmp_col = [colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b]
    col_matrix.append(tuple(tmp_col))

#Want 10 by 10 dot grid, spaced apart by 50 and 20 in size
#Need screen size of ~750 * 750

screen = Screen()
screen.colormode(255)
screen.setup(800, 800)

brush=Turtle()
brush.ht()
brush.speed(0)
#brush.width(0)




grid_size = 10
brush.pu()
brush.setpos(-350, -420)
row_hts = range(-350, 350, 70)

tick=0
for row in range(grid_size):
    brush.setpos(-350, row_hts[tick])
    tick+=1
    for dot in range(grid_size):
        brush.begin_fill()
        brush.fillcolor(random.choice((col_matrix)))
        brush.circle(20)
        brush.end_fill()
        brush.forward(70)




screen.exitonclick()
