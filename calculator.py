# Abubakar's Fresh Calculator

# Define operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

# Main loop
while True:
    print("\nChoose an operation:")
    print(" +  → Addition")
    print(" -  → Subtraction")
    print(" *  → Multiplication")
    print(" /  → Division")
    print(" %  → Modulus")
    print(" ** → Power")

    operation = input("Enter operation: ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "%":
        result = modulus(num1, num2)
    elif operation == "**":
        result = power(num1, num2)
    else:
        result = "Invalid operation"

    print("Result:", result)

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye, Abubakar!")
        break
