
#rock, paper, scissors
#input user
#generate answer
#set logic of game - for winning , lossing and tie with if and elif

import random

user = input("Enter a choice (rock, paper, scissors): ")

computer = ["rock", "paper", "scissors"]
random = random.choice(computer)
print(f"Your picked {user}, computer picked {random}.")

if user == random:
    print("It's a tie!")
elif user == "rock":
    if random == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif user == "paper":
    if random == "rock":
        print("You win!")
    else:
        print("You lose.")
elif user == "scissors":
    if random == "paper":
        print("You win!")
    else:
        print("You lose.")