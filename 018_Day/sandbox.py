from turtle import Turtle, Screen
import random

timmy = Turtle()
# timmy.shape("turtle")
timmy.ht()
timmy.width(5)
timmy.speed(10)
#timmy.color("black", "red")

#timmy.circle(100)


def draw_shape(target, size, num_sides=4, dash_state=False):
    """takes a turtle object (target) and draws a polygon of sides (num_sides) and length (size) on screen. Optionally takes 'dash state to dash lines'"""
    angle= 360 / num_sides
    for _ in range(num_sides):
        if not dash_state:
            target.forward(size)
        else:
            dist = 0
            if size > 0:
                dash_length = 10
            else:
                dash_length = -10
            
            residual= size % dash_length
            while dist < abs(size - dash_length):
                target.forward(dash_length)
                target.pu()
                target.forward(dash_length)
                target.pd()
                dist += 2*abs(dash_length)
            target.forward(residual)


        target.left(angle)


def get_random_color():
    """Returns random color as rgb triplet"""
    color = []
    for _ in range(3):
        color.append(random.randint(0, 200) / 255)
    return color

#draw_square(timmy, 100,7)
# draw_square(timmy,-200,dash_state=True)




# for i in range(2,10):
#     timmy.pencolor((get_random_color()))
#     if i % 2 == 0:
#         draw_shape(timmy, 100, i + 1, False)
#     else:
#         draw_shape(timmy,100,i+1,False)


for i in range(1000):
    timmy.pencolor((get_random_color()))
    num_turns = random.randint(0, 3)
    timmy.left(90*num_turns)
    timmy.forward(15)




screen=Screen()
screen.exitonclick()
