rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random as rd

user_choice=input("What is your choice? (rock, paper, or scissors)")
user_choice=user_choice.lower()

comp_choice=rd.randint(0,2) #0=rock, 1=paper, 2=scissors

print("User choice:")
if user_choice=="paper":
    print(paper)
elif user_choice=="rock":
    print(rock)
elif user_choice=="scissors":
    print(scissors)
else:
    print("Invalid option, you lose!")

print("Computer choice:")
if comp_choice==0:
    print(rock)
    if user_choice=="paper":
        print("You win!")
    elif user_choice=="rock":
        print("You tied!")
    elif user_choice=="scissors":
        print("You lose!")
elif comp_choice==1:
    print(paper)
    if user_choice=="paper":
        print("You tied!")
    elif user_choice=="rock":
        print("You lose!")
    elif user_choice=="scissors":
        print("You win!")
elif comp_choice==2:
    print(scissors)
    if user_choice=="paper":
        print("You lose!")
    elif user_choice=="rock":
        print("You win!")
    elif user_choice=="scissors":
        print("You tied!")
