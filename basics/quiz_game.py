questions = (
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the largest planet?",
    "What is the chemical symbol for gold?",
    "What year did World War II end?",
)

answers = (
    "Paris",
    "4",
    "Jupiter",
    "Au",
    "1945",
)

options = (
    ("1. Paris", "2. London", "3. Berlin", "4. Madrid"),
    ("1. 3", "2. 4", "3. 5", "4. 6"),
    ("1. Saturn", "2. Jupiter", "3. Mars", "4. Venus"),
    ("1. Au", "2. Ag", "3. Al", "4. Ar"),
    ("1. 1943", "2. 1944", "3. 1945", "4. 1946"),
)

question_num=0
for question in questions:
    print("-----------")
    print(question)
    for option in options[question_num]:
        print(option)
    user_input=int(input("enter the correct option: "))  
    if user_input==answers[question_num]:
        print("correct")
    else:
        print("incorrect")
        print("correct answer is",answers[question_num])      


    question_num+=1    