import random
from IPython.display import clear_output

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck"""
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_given = random.choice(cards)
    
    return card_given

def calculate_score(cards):
    """Take a list of cards and calculate the score"""
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # Blackjack
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
   
    return sum(cards)


def compare(user_score,computer_score):
    """Compares the user score and computer score"""
    if user_score == computer_score:
        return f"Push..."
    elif computer_score == 0:
        return f"You Lose, computer has Blackjack "
    elif user_score == 0:
        return f"Blackjack....You WIN !!!"
    elif user_score > 21:
        return f"You Lose....You Bust.."
    elif computer_score > 21:
        return f"You WIN....Computer Bust!!! "
    elif user_score > computer_score:
        return f"You WIN !!!, Your score is closer to 21 "
    else:
        return f"You Lose, computer score is closer to 21"

def play_game():
    """Starts the game"""
    print(logo)
    user_cards = []
    computer_cards = []   
    is_game_over = False

    for _ in range(2): 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User drawing cards
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer drawing cards
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score} ")
    print(f"Computer's final card: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_output(wait=True)
    play_game()
    
