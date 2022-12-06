import random

logo = """

  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 

"""

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to Compare number guessed against actual number
def compare(guessed_number,actual_number, number_of_attempts):
    """Checks Guessed number against actual number. Returns No. of attemps remaining"""
    if guessed_number < actual_number:
        print ("Too Low")
        print("Guess Again")
        return number_of_attempts -1
        
    elif guessed_number > actual_number:
        print("Too High")
        print("Guess Again")
        return number_of_attempts -1
        
    elif guessed_number == actual_number:
        print(f"You got it, The answer is {actual_number}")
        
# Make a function to set difficulty
def game_difficulty():
    """Sets the Attempts according to Game Difficaulty""" 
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == 'easy':
        return EASY_LEVEL
    
    elif difficulty == 'hard':
        return HARD_LEVEL
    
def game():
    print(logo)
    # Choosing a random number between 1 -100
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


    actual_number = random.randint(1,100)
    print(f"the correct answer is {actual_number}")

    
    number_of_attempts = game_difficulty()

    # repeat the guessing functionality
    guessed_number = 0
    while guessed_number != actual_number:
        
         # Track number of attempts and decrease by 1 if user gets it wrong
        print(f"You have {number_of_attempts} attemps remaining to guess the number.")
        
        # Let User guess a number
        guessed_number = int(input("Make a Guess: "))
        number_of_attempts = compare(guessed_number, actual_number, number_of_attempts) 
        
        if number_of_attempts == 0:
            print("You've run out of guesses, You Lose!")
            return

game()
