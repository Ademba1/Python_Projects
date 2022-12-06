
### Treasure Island

print("  ********* Welcome to Treasure Island ************      ")
print("    *** Player Beware, You're in for a scare! ***  \n\n\n")

print('''
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

''')
print("You have been walking on the shores on the beach, you pick a piece of paper lying there.\n")
print("You realise it is not just a treasure map, but 'THE TREASURE MAP', searched for millenia.\n")
print("The treasure at the 'X' is said to contain the Elixir of Youth!")

# Scenarios

beach = input('''
What do you choose to do?
A. Follow The Treasure!
B. Go Home!
''')


take_boat = '''
You get into the boat and start rowing.
A big wave hits you and

"YOU DIE!!"
'''

swim_swim = '''
You get into the water and start to swim.
You won the olympics swimming competition anyway.
OH Snap!

A Shark comes out of knowhere and Eats you alive.

"YOU DIE!!"
'''

burn_map = '''
You burn the map.
This is too creepy, you think.
Suddenly, you burst into flames and 

"YOU DIE!!"
'''

chew_map = '''
You find this funny!
To show the map who's Boss, you put it your mouth and chew it
OH that's actually pretty good. Tastes like chicken.


"YOU JUST ATE THE ELIXIR AND WILL BE YOUNG FOREVER!!"
'''


# Go for Treasure

if beach == "A" or beach == "a":
    direction_treasure = input('''
You are very excited. If you find the Elixir, you stay young forever.
Wow, that sounds awesome, you shout 'I AM GOING TO BE YOUNG FOREVER!!!'
The map begins to speak and asks you.

Map: "Greetings traveller,
        i hope you like the water, to go find the treasure, 
        will you take a boat or will you swim?"

A. Take boat!
B. Swim!
''')
    if direction_treasure == "A" or direction_treasure == "a":
        print(take_boat)
        
    elif direction_treasure == "B" or direction_treasure == "b":
        print(swim_swim)
    else:
        print("Wrong Entry, Start Again!")

# Go Home

elif beach == "B" or beach =="b":
    direction_home = input('''
You place the map in your bag and go home.
Once you get home, the map begins to speak and instructs you to look at it.
You take it out and It gives you a choice:

A. Follow The Treasure!
B. Burn the Map!
C. Chew the map for laughs
''')

    if direction_home == "A" or direction_home == "a":
        direction_treasure = input('''
You are very excited. If you find the Elixir, you stay young forever.
Wow, that sounds awesome, you shout 'I AM GOING TO BE YOUNG FOREVER!!!'
The map begins to speak and asks you.

Map: "Greetings traveller,
        i hope you like the water, to go find the treasure, 
        will you take a boat or will you swim?"

A. Take boat!
B. Swim!
''')
        if direction_treasure == "A" or direction_treasure =="a":
            print(take_boat)

        elif direction_treasure == "B" or direction_treasure =="b":
            print(swim_swim)
        else:
            print("Wrong Entry, Start Again!")
        
    elif direction_home == "B" or direction_home == "b":
        print(burn_map)
    
    elif direction_home == "C" or direction_home == "c":
        print(chew_map)
