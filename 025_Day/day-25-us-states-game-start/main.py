import turtle
import pandas

data=pandas.read_csv('50_states.csv')

IMG_FILE='blank_states_img.gif'
screen = turtle.Screen()
screen.title("US States Quiz Game")
screen.addshape(IMG_FILE)
turtle.shape(IMG_FILE)

num_correct=0
active_states = data
while num_correct < len(data):
    title_text=f"Guess the state! {num_correct} / {len(data)}"
    answer_state = screen.textinput(title=title_text, prompt="Enter a state: ")

    as_names = active_states.state
    for state in as_names:
        if state.lower() == answer_state.lower():
            num_correct+=1
            drop_idx=active_states[active_states.state == state].index[0]
            
            new_turtle=turtle.Turtle(visible=False)
            new_turtle.pu()
            new_turtle.goto(active_states.x[drop_idx],active_states.y[drop_idx])
            new_turtle.write(state)

            active_states = active_states.drop(drop_idx)

    if answer_state == 'exit':
        active_states.to_csv("Unguessed States.csv")
        break



screen.mainloop()
