options=["1", "2", "3", "4", "5"]

print("***** CALCULATOR *****")

while True:
    print("\nChoose one of the following actions:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")

    user_input=input("Enter your choice (1-5): ")

    while user_input not in options:
        print("Invalid input")
        user_input=input("Enter your choice (1-5): ")

    if user_input=="5":
        print("Thanks for using the calculator")
        break   

    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))

    if user_input=="1":
        print("Sum:",a + b)

    elif user_input=="2":
        print("Difference:",a - b)

    elif user_input=="3":
        print("Multiplication:",a * b)

    elif user_input=="4":
        while b==0:
            print("Second number cannot be 0")
            b=int(input("Enter the second number again: "))
        print("Division:",a / b)





 
        
  

               