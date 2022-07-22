## BLIND AUCTION

import art
print(art.logo)

#first create an EMPTY dictionary so we can add (APPEND) values later in the existing one
auction ={}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What's the name of the bidder?: ")
    price = int(input("What's your bidding amount?: $"))
    auction[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(auction)
