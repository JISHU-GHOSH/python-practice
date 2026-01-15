word="apple"

letter=input("enter a letter in secret word: ")

if letter in word:# not in interchange print statement
    print(f"{letter} was correct")
else:
    print(f"{letter} not in word")

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

name=input("enter student name: ")
if name not in names:
    print(f"{name} not found")
else:
    print(f"{name} was found") 


students = {
            "Alice": 85,
            "Bob": 92,
            "Charlie": 78,
            "Diana": 88,
            "Eve": 95
        }
student=input("enter student name: ")
if student in students:
    print(f"{student} marks is{student[students]}")
else:
    print(f"{student} not in data")    

