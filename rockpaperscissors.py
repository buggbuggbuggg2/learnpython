import random

while True:
    print("lets play rock, paper, scissors! (or q to exit) first turn, go!")
    user_action = input("what dyu choose? (rock, paper, scissors, q): ")

    if user_action == "quit" or user_action == "q":
        print("thanks for playing! bye.")
        break

    bot_choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(bot_choices)

    print(f"you selected {user_action}, and i chose {bot_choice}.")

    if user_action == bot_choice:
        print("oops! its a tie!")
    elif user_action == "rock":
        if bot_choice == "scissors":
            print("you win!")
        else:
            print("you lose...")
    elif user_action == "paper":
        if bot_choice == "rock":
            print("you win!")
        else:
            print("you lose...")
    elif user_action == "scissors":
        if bot_choice == "paper":
            print("you win!")
        else:
            print("you lose...")