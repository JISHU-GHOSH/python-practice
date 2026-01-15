##*args tuple
## **kwargs dictionary

def add(*args):
    total=0
    for arg in args:
        total+=arg
    print(total) 
#add(2,6,3,8,9)
def display_name(*names):
    for name in names:
        print(name,end=" ")
#display_name("mr","william","butcher") 

def location(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        pass
"""
location(street="bus stand",
         pin=735214,
         city="kalchini",
         state="west bengal")
"""                        


def id(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()    
    for value in kwargs.values():
        print(value,end=" ")    

id("dr","hamilton","butcher",
      street="bus stand",
         pin=735214,
         city="kalchini",
         state="west bengal")