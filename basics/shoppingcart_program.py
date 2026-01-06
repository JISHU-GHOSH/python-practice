foods=[]
price=[]
total=0

while True:
    user_input=input("enter the food you want to buy(q to quit): ")
    if user_input=="q":
        break
    else:
        quantity=int(input("how many do you want to buy: "))
        money=float(input("enter the prize of the food: "))
        total_money=quantity*money
        foods.append(user_input)
        price.append(total_money)

print("----CART----")

for i in range(len(foods)):
    print(f"{foods[i]}: ${price[i]:.2f}")

total = sum(price)
print(f"Total: ${total:.2f}")
