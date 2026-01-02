age=int(input("enter your age: "))


if age<18:
    print("the applicant is underage thus cant vote")
elif age>=18 and age<80:
    document=input("type(yes) if you have voter card (no) if you dont have: ")
    if document=="yes":
        print("the person is eligible to vote")
    else:
        print("the person is not eligible to vote")
else:
    print("too old to vote")            
        