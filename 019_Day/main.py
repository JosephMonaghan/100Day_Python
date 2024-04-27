from turtle import Turtle, Screen
import random

screen=Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Place your bets!",prompt="Which turtle do you think will win (enter a color)?")


colors=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
num_turtles=len(colors)

turtle_racers=[]
start_y=range(-150,150,int(300/num_turtles))
for turtle in range(num_turtles):
    turtle_racers.append(Turtle(shape='turtle'))
    turtle_racers[turtle].speed("fast")
    turtle_racers[turtle].color(colors[turtle])
    turtle_racers[turtle].pu()
    turtle_racers[turtle].goto(x=-230,y=start_y[turtle])

max_pos=-230
leader=""


while max_pos < 200:
    for turtle in range(len(turtle_racers)):
        turtle_racers[turtle].pd()
        turtle_racers[turtle].forward(random.randint(0,10))
        cur_pos = turtle_racers[turtle].pos()
        if cur_pos[0] > max_pos:
            max_pos=cur_pos[0]
            leader=turtle_racers[turtle].color()

        #Random headings so the turtles are wobbly :)
        cur_heading=turtle_racers[turtle].heading()
        if cur_heading == 0:
            turtle_racers[turtle].setheading(0 + random.randint(0,15))
        elif cur_heading > 0 and cur_heading < 35:
            turtle_racers[turtle].right(random.randint(0,15))
        elif cur_heading > 340:
            turtle_racers[turtle].left(random.randint(0,15))
        

if user_bet.lower==leader[0].lower:
    print(f"Awesome, you won! The {leader[0]} turtle won the race.")
else:
    print(f"Sorry, you lost (womp womp). The {user_bet} turtle lost and the {leader[0]} turtle won the race.")

screen.exitonclick()