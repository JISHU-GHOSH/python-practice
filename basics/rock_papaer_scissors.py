import random

choices=["rock","paper","scissors"]

choice=random.choice(choices)

while True:
    print("welcome to the game of rock paper scissors")
    user_input = input("enter your choice: ")
    
    if user_input not in choices:
        print("invalid choice")
        continue
    print(f"computer choice was {choice}")
    if user_input=="rock" and choice=="scissors":
        print("yeah you won")
    elif user_input=="paper" and choice=="rock":
        print("yeah you won")
    elif user_input=="scissors"and choice=="paper":
        print("yeah you won")
    elif user_input==choice:
        print("it's a tie")
    else:
        print("you lost")

 
    play_again = input("play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("thanks for playing")
        break
    
    choice = random.choice(choices)


    