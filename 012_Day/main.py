import os
from art import logo
import random

os.system("Clear")
print(logo)

def choose_number():
    """Defines the random number between 1 and 100"""
    num=random.choice(range(100))+1
    return num

def assign_lives(game_mode):
    """Assigns number of lives based on chosen difficulty, dev mode gives effectively infinite lives"""
    if game_mode=='easy':
        return 10
    elif game_mode=='hard':
        return 5
    elif game_mode=='dev':
        return 9999

def check_guess(val,target):
    """Evaluates the guess against the chosen number and returns whether they need to go higher, lower, or got it"""
    if val==target:
        return "Correct"
    elif val < target:
        return "Too low"
    elif val > target:
        return "Too high"

def remove_live(lives):
    """Removes one from remaining lives"""
    global keep_playing, eval_guess
    lives-=1
    if lives < 1:
        print("You've run out of guesses, you lose!")
        keep_playing=False
    else:
        print(eval_guess)
    return lives

hidden_num=choose_number()

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 & 100.")
#print(f"Pssst, the correct number is {hidden_num}")

game_mode=input("Choose a difficulty, type 'easy' or 'hard':  ")

num_lives=assign_lives(game_mode)

keep_playing=True

while keep_playing:
    print(f"You have {num_lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    eval_guess=check_guess(guess,hidden_num)
    
    if not eval_guess=="Correct":
        num_lives=remove_live(num_lives)
    else:
        print(f"You got it! The answer is {hidden_num}")
        keep_playing=False
    

    








