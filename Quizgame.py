def again():
    print('\n')
    option = "b"
    print("1. What is the capital of Brazil?")
    print("Options: a) Rio de Janeiro   b) Brasília   c) São Paulo   d) Salvador")
    choice = input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option, choice)

    option = "a"
    print("2. What is the capital of Thailand?")
    print("Options: a) Bangkok   b) Chiang Mai   c) Phuket   d) Pattaya")
    choice = input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option, choice)

    option = "b"
    print("3. What is the capital of Canada?")
    print("Options: a) Toronto   b) Ottawa   c) Vancouver   d) Montreal")
    choice = input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option, choice)

    option = "d"
    print("4. What is the capital of Australia?")
    print("Options: a) Sydney   b) Melbourne   c) Brisbane   d) Canberra")
    choice = input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option, choice)

    option = "c"
    print("5. What is the capital of Egypt?")
    print("Options: a) Cairo   b) Alexandria   c) Luxor   d) Giza")
    choice = input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option, choice)

    print(f"You have scored {score} points out of 20")


def scorer():
    global score
    score+=2


def checker(option,choice):
    if choice==option:
        print("Correct answer")
        print('\n')
        scorer()
    else:
        print(f"Incorrect answer, the correct answer is option '{option}'")
        print('\n')


def questions():
    global score
    score=0
    option="a"
    print("1. What is the capital of United States")
    print("Options: a) Washington, D.C.   b) New York City   c) Los Angeles   d) Chicago")
    choice=input("Enter only the option of the answer: ")
    choice=choice.lower()
    checker(option, choice,)

    option="a"
    print("2. What is the capital of China?")
    print("Options: a) Beijing   b) Shanghai   c) Guangzhou   d) Hong Kong")
    choice=input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option,choice)

    option="c"
    print("3. What is the capital of India?")
    print("Options: a) Bangalore   b) Mumbai   c) New Delhi   d) Chennai")
    choice=input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option,choice)

    option="d"
    print("4. What is the capital of Indonesia?")
    print("Options: a) Medan   b) Surabaya   c) Bandung   d) Jakarta")
    choice=input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option,choice)

    option="b"
    print("5. What is the capital of Pakistan?")
    print("Options: a) Karachi   b) Islamabad   c) Lahore   d) Faisalabad")
    choice=input("Enter only the option of the answer: ")
    choice = choice.lower()
    checker(option,choice)

    print(f"You have scored {score} points out of 10")
    print('\n')
    re=(input("Press 'y' is you want to play again and 'n' to exit: "))
    if re=='y' or re=='Y':
        again()
    if re=='n' or re=='N':
        print("Thank you for playing :)")


print('\n')
print("****************************************************WELCOME TO THE QUIZ GAME OF GUESS THE CAPITALS OF THE COUNTRY*********************************************************")
print('\n')
print("Rules and regulations:")
print("1.There are five questions.")
print("2.Enter only the option of the question to select an answer.")
print("3.For each right answer, you will get 2 points.")
print("4.Similarly, you will get 0 points for the wrong answer.")
print('\n')
print("Good luck!")
print('\n')
questions()

