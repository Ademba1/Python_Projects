logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo,"\n")
print("Welcome to the Secret Auction Program\n")

def find_highest_bidder(bidding_record):
    
    highest_bid =0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print (f"The winner is {winner} with a bid of ${highest_bid}.")

bids= {}
more_bidders =True 
while more_bidders:  
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n $"))
    
    bids[name] = price
    
    next_bidder = input("Are there any other bidders?Type 'yes' or 'no'.\n")
    
    if next_bidder == "no":
        more_bidders = False
        find_highest_bidder(bids)
        print(bids)

