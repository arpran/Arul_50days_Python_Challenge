# Basic Calculator Script

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Display the available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for operation
operation = input("Enter choice (1/2/3/4): ")

# Take user input for the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the calculation based on the chosen operation
if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input! Please select a valid operation (1/2/3/4).")
