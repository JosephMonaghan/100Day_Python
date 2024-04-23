from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "red")

#timmy.circle(100)


def draw_square(target, size):
    """takes a turtle object (target) and draws a square of length (size) on screen"""
    for _ in range(4):
        target.forward(size)
        target.left(90)


draw_square(timmy, 100)
draw_square(timmy,-200)






screen=Screen()
screen.exitonclick()
