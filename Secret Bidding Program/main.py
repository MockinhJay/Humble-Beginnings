from clearFunction import clear
from art import logo

continuing_bid = True
bidding_log = {}
highest_bid = 0
winner = ""

print(logo)
  
while continuing_bid:
  #Taking input and adding to the dictionary
  name = input("What is your Name?\n")
  bidding_amount = int(input("How much money do you want to bid? $"))
  bidding_log[name] = bidding_amount
  more_bids = input("Are there any bidders? Type 'yes' or 'no'.\n")
  #Should continue or not
  if more_bids == "yes":
    clear()
  elif more_bids == "no":
    continuing_bid = False
    clear()
    print("Bidding has stopped")
    #Looking for the highest bidder in the dictionary
    for people in bidding_log:
      bid = bidding_log[people]
      if bid > highest_bid:
        highest_bid = bid
        winner = people
    print(f"The highest bidder is {winner}, with a bid of ${highest_bid}.\n")
