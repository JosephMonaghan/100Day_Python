# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color('black', 'purple')
# fred = turtle.Turtle()
# fred.shape('turtle')
# fred.color('black','green')


# def draw_triangle(target, direction, size):
#     size*=direction
#     target.forward(size)
#     target.left(120)
#     target.forward(size)
#     target.left(120)
#     target.forward(size)


# draw_triangle(timmy, 1, 100)
# draw_triangle(fred,-1,200)


# my_screen = turtle.Screen()

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type",["Electric","Water","Fire","Grass"])
table.align = "c"
table.padding_width = 5
table.

print(table)
