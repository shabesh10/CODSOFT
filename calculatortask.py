def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    if b==0:
        return "Error! You are dividing by zero!"
    return a/b
def mul(a,b):
    return a*b
def mod(a,b):
    return a%b

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    print("5.Modulo")
    print("6.Exit")
    choice = int(input("Please select an operation from above:"))
    if choice<6:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        if choice == 1:
            print(f"{a} + {b} =", add(a, b))
            print("************************")
        elif choice == 2:
            print(f"{a} - {b} =", sub(a, b))
            print("************************")
        elif choice == 3:
            print(f"{a} / {b} =", div(a, b))
            print("************************")
        elif choice == 4:
            print(f"{a} * {b} =", mul(a, b))
            print("************************")
        elif choice == 5:
            print(f"{a} % {b} =", mod(a, b))
            print("************************")
    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid input! Please try again.")
        print("************************")





