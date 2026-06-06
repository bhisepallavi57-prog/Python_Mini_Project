# Simple Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def avg(num1, num2):
    return (num1 + num2) / 2


while True:

    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Average")
    print("6. Exit")

    try:
        select = int(input("Select operation (1-6): "))

        if select == 6:
            print("Calculator Closed.")
            break

        if select not in [1, 2, 3, 4, 5]:
            print("Invalid Choice! Please select between 1 and 6.")
            continue

        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if select == 1:
            print(f"{number_1} + {number_2} = {add(number_1, number_2)}")

        elif select == 2:
            print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")

        elif select == 3:
            print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")

        elif select == 4:
            print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")

        elif select == 5:
            print(f"Average of {number_1} and {number_2} = {avg(number_1, number_2)}")

    except ValueError:
        print("Please enter valid numeric values.")
