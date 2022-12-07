from art import logo,vs
from game_data import data
from random import choice
from IPython.display import clear_output


def format_data(account):
    """
    Takes the Account Data. Returns the printable format.
    
    Parameters
    ----------
    account : The account data Dictionary 
    
    Examples
    --------
    >>> format_data({
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    )
    
    out: Instagram, a Social media platform, from United States
    
    >>> format_data({
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    )
    
    out: Cristiano Ronaldo, a Footballer, from Portugal
    
    """

    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
#     account_follower_count = account['follower_count']
    
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, A_followers, B_followers):
    """
    Takes Users guess and follower counts of A and B. Returns if the got it right
    
     Parameters
     -----------
     guess : Users Guess
     A_followers: The Follower count of account_A
     B_followers: The Follower count of account_B
     
     
    
    """
    if A_followers > B_followers:
        return guess == 'a'
    else:
        return guess == 'b'

    
# Display art
print(logo)
score = 0
game_should_continue = True

# Making the accounts at B become the next account at A
account_B = choice(data)

# If User is right Repeat game
while game_should_continue:
    # Generate random account
    account_A = account_B
    account_B = choice(data)

    while account_A == account_B:
        account_B = choice(data)


    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")

    # Ask user to make guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # Check if user is correct
    ## Get follower count of each accunt
    ## Use if statement to check if user is correct

    A_follower_count = account_A['follower_count']
    B_follower_count = account_B['follower_count']
    is_correct = check_answer(guess, A_follower_count, B_follower_count)
    
    
    # Clear the screen
    clear_output()
    print(logo)
    # Give User Feedback
    # Score keeping
    if is_correct:
        score +=1
        print(f"\nYou're right! Current score: {score}")

    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
        
