
#Import logo art, game data, os commands, random module
import os
from art import logo,vs
from gamedata import data
import random

##Personal high score = 15
INITIAL_SCORE=0

#Grab an A choice and a B choice randomly from game_data
def update_choices(game_state,ChB):
    """Returns choice A and B from the game data"""
    global data
    if game_state==0:
        choice_A=random.choice(data)
        choice_B=random.choice(data)
    else:
        choice_A=ChB
        choice_B=random.choice(data)
        
    while choice_A == choice_B: #Rerolls choice B if they happen to roll to the same val
        choice_B=random.choice(data)
    return choice_A,choice_B

    


#Display logo, then A choice, then vs. art, then B choice
def update_display(A_choice, B_choice,cur_score):
    global logo, vs
    #Clear screen each time for clear window
    os.system('Clear')
    print(logo)
    if cur_score > 0:
        print(f"You're right! current score: {cur_score}.")
    
    print(f"Compare A: {A_choice['name']}, a {A_choice['description']} from {A_choice['country']}.")
    print(vs)
    print(f"To B: {B_choice['name']}, a {B_choice['description']} from {B_choice['country']}.")

#Get the game to go again if user was right
def eval_choice(OptionA,OptionB,user_input):
    A_followers=OptionA['follower_count']
    B_followers=OptionB['follower_count']
    if A_followers > B_followers:
        corr_choice="A"
    else:
        corr_choice="B"
    
    if corr_choice==user_input:
        return True
    else:
        return False  

#Place the overall game in a function

hold_ChB=""
def game(score):
    global hold_ChB

    ChA,ChB=update_choices(score,hold_ChB)
    
    update_display(ChA,ChB,score)
    #Ask user for input on whether they think A or B is higher
    user_choice=input("Which do you think is has more followers, A or B?  ").upper()
    is_correct=eval_choice(ChA,ChB,user_choice)
    if is_correct:
        #Keep track of score - how many in a row has user gotten right
        score+=1
        #Hold choice B for next round
        hold_ChB=ChB
        #Get the game to go again if user was right
        game(score)
    else:
        #Stop the game and tell user their final score if wrong
        return print(f"You guessed wrong and got a final score of {score}")
game(0)








