import os

from art import logo

keep_collecting_bids=True
bid_library={}

while keep_collecting_bids:
    os.system('Clear')
    print(logo)
    print("Welcome to the secret auction program.")
    name=input("What is your name?")
    bid=int(input("What is your bid? $"))
    bid_library[name]=bid

    other_bidders=input("Are there any other bidders? (Y/N)")
    if other_bidders=="N":
        keep_collecting_bids=False

os.system('Clear')
max_bid=0
for each_bid in bid_library:
    if bid_library[each_bid] > max_bid:
        winning_bidder=each_bid
        max_bid=bid_library[each_bid]

print(logo)
print(f"{winning_bidder} won the auction with a bid of ${max_bid}")