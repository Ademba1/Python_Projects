### Rock, Paper, Scissors

import random
rock = '''
 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
'''
paper = '''
       _.-._
      | | | |_
      | | | | |
      | | | | |
    _ |  '-._ |
    \`\`-.'-._;
     \    '   |
      \  .`  /
       |    |

'''
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

'''

game_rps = ["Rock", "Paper", "Scissors"]

try:
    user_Choice = game_rps[int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))]
    if user_Choice == "Rock":
        print(rock)
    elif user_Choice == "Paper":
        print(paper)
    elif user_Choice == "Scissors":
        print(scissors)

    random_choice = random.choice(game_rps)
    print("Computer chose:")
    if random_choice == "Rock":
        print(rock)
    elif random_choice == "Paper":
        print(paper)
    elif random_choice == "Scissors":
        print(scissors)

    # Paper Win

    if user_Choice == "Rock" and random_choice == "Paper":
        print("You Lose")
    elif user_Choice == "Paper" and random_choice == "Rock":
        print("You Win")

    # Rock Win

    elif user_Choice == "Scissors" and random_choice == "Rock":
        print("You Lose")
    elif user_Choice == "Rock" and random_choice == "Scissors":
        print("You Win")

    # Scissors Win

    elif user_Choice == "Paper" and random_choice == "Scissors":
        print("You Lose")
    elif user_Choice == "Scissors" and random_choice == "Paper":
        print("You Win")
    elif user_Choice == random_choice:
        print("It is a Draw")
except IndexError:
    print("You typed an Invalid number; You Lose!")



