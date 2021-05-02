import time

import random

MONSTER_NAMES = ["bog monster", "snake monster", "hairy monster", "giant scorpion monster", "troll", "shadow monster"]
SLEEP_TIME = 2

# Game state
state = ""
monster_name = ""
has_sword = False
killed_monster = False

def reset_game_state():
    global state
    global monster_name
    global has_sword
    global killed_monster
    state = "start"
    monster_name = get_random_monster()
    has_sword = False
    killed_monster = False

def get_random_monster():
    random_index = random.randint(0, len(MONSTER_NAMES))-1
    random_monster_name = MONSTER_NAMES[random_index]
    return random_monster_name

def print_wait(input):
    print(input)
    time.sleep(SLEEP_TIME)

def start():
    global state
    global monster_name
    print_wait("You find yourself in the middle of a dark and rainy forest. "
    f"A {monster_name} has been terrorizing the folk of a nearby town and could be lurking behind any tree... ")
    print_wait("You can see a cave in the distance. Suddenly, you hear a scream of distress! "
    "You run towards the dark cave and you hear another scream. To the right of the cave "
    "is a chest that may contain a weapon.")
    print_wait("Enter 1 to enter the cave.")
    print_wait("Enter 2 to check the chest on the right.")
    print_wait("What would you like to do?")
    state = "cave_or_sword"

def cave_or_sword():
    global state
    print_wait("Please enter 1 or 2.")
    player_input = input("")
    if player_input == "1":
        state = "cave"
    elif player_input == "2":
        state = "get_sword"
    else:
        print_wait("I don't understand. Please try again.")

def cave():
    global state
    global killed_monster
    global monster_name
    print_wait("You enter the dark cave, lighting a torch to guide you, until you reach a huge cavern.")
    if not has_sword:
        print_wait(f"There is something behind you! You do not have a weapon to defend yourself and are killed by the {monster_name}.")
        state = "game_over"
    else:
        print_wait(f"The magical sword's power was too great for the {monster_name}! You've vanquished your foe triumphantly!")
        killed_monster = True
        state = "town"

def get_sword():
    global has_sword
    global state
    print_wait("The chest pops open easily to reveal a magnificent long silver blade. The likes of which you have never seen. "
    "The sword glows with a hint of magic. Now you are ready to investigate the cave.")
    has_sword = True
    print_wait("Press 1 to enter the cave with the sword. Press 2 to return to town.")
    player_input = input("")
    if player_input == "1":
        state = "cave"
    elif player_input == "2":
        state = "town"
    else:
        print_wait("I don't understand. Please try again.")

def town():
    global state
    global killed_monster
    if not killed_monster:
        print_wait("The townspeople were distrustful of your sword and chased you out! You lose!")
        state = "game_over"
    else:
        print_wait("You enter the town victorious and the townspeople throw a party at the local pub to celebrate!")
        state = "game_over"

def game_over():
    global state
    print_wait("Do you want to play again? Y or N")
    player_input = input("").lower()
    if player_input == "y":
        reset_game_state()
    elif player_input == "n":
        state = "end"
    else:
        print_wait("I don't understand. Please try again.")

def play_game():
    global state
    global monster_name
    global has_sword
    global killed_monster
    reset_game_state()
    while True:
        if state == "start":
            start()
        elif state == "cave_or_sword":
            cave_or_sword()
        elif state == "cave":
            cave()
        elif state == "get_sword":
            get_sword()
        elif state == "town":
            town()
        elif state == "game_over":
            game_over()
        else:
            return

play_game()
