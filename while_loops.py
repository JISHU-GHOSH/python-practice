num=int(input("enter a number between 1-10: "))
while num<1 or num>10:
    print("invalid input")
    num=int(input("enter a number between 1-10: "))
print("the number you enter is",num)    