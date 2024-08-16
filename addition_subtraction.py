# Function to validate input as a number
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Part 1: Addition and Subtraction

# Asking the user to input two numbers
num1 = get_valid_number("Enter the first number: ")
num2 = get_valid_number("Enter the second number: ")

# Performing addition
addition_result = num1 + num2

# Performing subtraction
subtraction_result = num1 - num2

# Displaying the results
print("Addition of", num1, "and", num2, "is:", addition_result)
print("Subtraction of", num2, "from", num1, "is:", subtraction_result)
