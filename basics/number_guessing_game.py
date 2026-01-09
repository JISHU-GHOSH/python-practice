import random

low=1
high=50
guess=0

secret_number=random.randint(low, high)
print("guess the number between 1 to 50")

while True:
    user_input=input("enter your number: ")
    
    if user_input.isdigit():
        user_input=int(user_input)
        if low<=user_input<=high:
            if secret_number==user_input:
                print("that was correct!")
                break
            else:
                guess+=1
                if user_input>secret_number:
                    print("your guess is too high, try again")
                else:
                    print("your guess is too low, try again")
        else:
            print(f"please enter a number between {low} and {high}")
    else:
        print("invalid input! Please enter a valid number")
print(f"you took {guess} to guess the number")        
