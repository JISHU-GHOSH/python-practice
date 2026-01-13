def price_calculator(price,discount=0,tax=0.05):
    return price *(1-discount)*(1+tax)

print(price_calculator(5000,0.5,0.5)) #normal entry
print(price_calculator(500))#default arguments used