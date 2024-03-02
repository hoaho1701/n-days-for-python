#from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")
# function of finding the winner and the highest bid
bids = {}
def finding_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
# function of recording bid
bid_finish = False
while not bid_finish:
  your_name = input("What is your name?: ")
  your_bid = input("What's your bid?: $")
  bids[your_name] = int(your_bid)
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == 'no':
    bid_finish = True
    finding_highest_bidder(bids)
  else:
    #clear()
    bid_finish = False