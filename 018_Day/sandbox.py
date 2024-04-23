from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "red")

#timmy.circle(100)


def draw_square(target, size, dash_state=False):
    """takes a turtle object (target) and draws a square of length (size) on screen. Optionally takes 'dash state to dash lines'"""
    for _ in range(4):
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


        target.left(90)


draw_square(timmy, 100)
draw_square(timmy,-200,True)






screen=Screen()
screen.exitonclick()
