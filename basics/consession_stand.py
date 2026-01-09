menu = {
    "hot dog": 5.00,
    "hamburger": 7.50,
    "pizza slice": 4.25,
    "popcorn": 3.50,
    "nachos": 6.00
}
cart=[]
total=0

print("-----MENU-----")
for food,price in menu.items():
    print(f"{food} : ${price:.2f}")
print("---------------")    

while True:
    food=input("enter the food you want to get(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


for food in cart:
    total+=menu.get(food)


print(f"your totoal was ${total:.2f}")