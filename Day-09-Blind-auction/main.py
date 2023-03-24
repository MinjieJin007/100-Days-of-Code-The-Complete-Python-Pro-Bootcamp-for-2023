from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
continue_bid = True
bid = {}
while continue_bid == True:
  name = input("What is your name?")
  bid[name] = int(input("What's your bid?: $"))
  continue_bid_ys = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if continue_bid_ys != "yes":
    continue_bid = False
  clear()
winner = ""
winner_bid = 0
for name in bid:
  bid_sum = bid[name]
  if bid_sum > winner_bid:
    winner_bid = bid_sum
    winner = name
print(f"The winner is {winner} with a bid of ${winner_bid}")

 

    
  
  
  