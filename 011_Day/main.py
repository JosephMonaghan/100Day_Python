############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
import os
from art import logo

os.system("Clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)
    
blackjack=input("Do you want to play a game of blackjack? (y for yes, n for no)")
if blackjack=="y":
    play_blackjack=True

def print_game_state(your_cards, dealer_cards):
    print(f"Your_cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")

def start_game():
    your_cards=[]

    your_cards.append(draw_card())
    your_cards.append(draw_card())

    dealer_cards=[]
    dealer_cards.append(draw_card())
    dealer_cards.append(draw_card())
    print_game_state(your_cards,dealer_cards)
    return your_cards, dealer_cards




def draw_cycle(player_cards,dealer_deck):
    draw_prompt=input("Type 'y' to get another card, type 'n' to pass:")
    
    while draw_prompt=='y':
        player_cards.append(draw_card())
        
        if sum(player_cards) > 21:
            for card in player_cards:
                has_ace=False
                if card==11:
                    has_ace=True
                    ace=player_cards.index(card)
            if not has_ace:
                game_state="bust"
                return player_cards, dealer_deck, game_state
            if has_ace:
                player_cards[ace]=1
            
        print_game_state(player_cards,dealer_deck)    
        draw_prompt=input("Type 'y' to get another card, type 'n' to pass:")

    game_state="inPlay"
    return player_cards, dealer_deck,game_state
        

while play_blackjack:
    os.system("Clear")
    print(logo)
    [your_cards, dealer_cards]=start_game()
    #Override:
    #dealer_cards=[11, 2]
    if sum(your_cards) == 22:
        your_cards[1]=1
    if sum(dealer_cards) == 22:
        dealer_cards[1]=1
    [your_cards, dealer_cards, game_state]=draw_cycle(your_cards,dealer_cards)
    if game_state=="bust":
        print("BUST, you drew over 21!")
    
    elif game_state=="inPlay":
        while sum(dealer_cards) < 17:
            dealer_cards.append(draw_card())
            if sum(dealer_cards) > 21:
                for card in dealer_cards:
                    has_ace=False
                    if card==11:
                        has_ace=True
                        ace=dealer_cards.index(card)
                    
                if has_ace:
                    dealer_cards[ace]=1
                else:
                    game_state="DealerBust"

    if game_state=="DealerBust":
        print("Dealer BUSTED, you win!")
        
    elif game_state=="inPlay":
        print(f"Your final hand: {your_cards}, score of {sum(your_cards)}")
        print(f"Computer's final hand: {dealer_cards}, score of {sum(dealer_cards)}")
        if sum(your_cards) > sum(dealer_cards):
            print("Congratulations, you win!")
        elif sum(your_cards) < sum(dealer_cards):
            print("Sorry, the dealer beat you")
        elif sum(your_cards) == sum(dealer_cards):
            if len(your_cards) < len(dealer_cards):
                print("Congratulations, you win!")
            elif len(your_cards) > len(dealer_cards):
                print("Sorry, the dealer beat you")
            elif len(your_cards) == len(dealer_cards):
                print("You and the dealer tied!")
        
    blackjack=input("Do you want to play a game of blackjack? (y for yes, n for no)")
    if blackjack=="n":  
        play_blackjack=False