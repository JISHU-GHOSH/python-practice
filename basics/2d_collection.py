"""
fruits=["apple","manago","pineapple"]
vegetables=["potatao","carrot","onion"]
meat=["chicken","mutton","pork"]

groceries=[fruits,vegetables,meat]


for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()    
"""
dial_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#"),
)


for num in dial_pad:
    for digit in num:
        print(digit,end=" ")
    print()    