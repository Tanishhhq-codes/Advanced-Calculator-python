import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number!"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0:
        return "Error: Logarithm not defined for non-positive values!"
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("""
    Select an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Power (^)
    6. Square Root (√)
    7. Logarithm (log)
    8. Sine (sin)
    9. Cosine (cos)
    10. Tangent (tan)
    0. Exit
    """)

    while True:
        choice = input("Enter choice (0-10): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"√{num} = {square_root(num)}")

        elif choice == '7':
            num = float(input("Enter number: "))
            base = float(input("Enter base (e.g., 10 for common log): "))
            print(f"log_{base}({num}) = {logarithm(num, base)}")

        elif choice == '8':
            num = float(input("Enter angle in degrees: "))
            print(f"sin({num}) = {sine(num)}")

        elif choice == '9':
            num = float(input("Enter angle in degrees: "))
            print(f"cos({num}) = {cosine(num)}")

        elif choice == '10':
            num = float(input("Enter angle in degrees: "))
            print(f"tan({num}) = {tangent(num)}")

        else:
            print("Invalid input. Please enter a valid choice!")

# Run the calculator
calculator()
