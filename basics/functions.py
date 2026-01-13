def happy_birthday(name,age):
    print(f"happy birthday {name} you are now {age} years old")



happy_birthday("lol",18)    

def account_statement(name,amount_due,time_left):
    print(f"Hi mr.{name} your amount due of ${amount_due} is to be payed within {time_left} days")


account_statement("fig",5254,5)


def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

name1="jishu"
name2="ghosh"

print(create_name(name1,name2))