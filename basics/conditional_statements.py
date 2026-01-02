base_price=12
coupon_code="SUPER_SAVER"

age=70


user_age=int(input("enter your age: "))

if user_age<13:
    ticket_price=8
    print("category:children")
elif user_age>=65:
    ticket_price=7
    print("category:senior")
else:
    ticket_price=12
    print("category: adult")

movie_time=int(input("enter movie hour(example:13 for 13.00pm show): "))
if movie_time<17:
    ticket_price=ticket_price-2
    print("discount applied $2 for movie before 17.00")

user_question=input("type (y) if you have promocode and enter anyother key if you dont have any: ")
if user_question=="y":
    promocode=input("enter your promocode: ")
    if promocode==coupon_code:
        ticket_price=ticket_price*0.9
        print("promocode applied: 10% off")
        print("your final ticket price is",ticket_price)
    else:
        print("invalid promocode")
else:
    print("your final ticket price is $",ticket_price)                     