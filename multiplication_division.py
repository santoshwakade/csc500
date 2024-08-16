# Function to validate input as a number
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Part 2: Multiplication and Division

# Asking the user to input two numbers
num1 = get_valid_number("Enter the first number: ")
num2 = get_valid_number("Enter the second number: ")

# Performing multiplication
multiplication_result = num1 * num2

# Performing division
# Check if num2 is not zero to avoid division by zero error
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "undefined (division by zero is not allowed)"

# Displaying the results
print("Multiplication of", num1, "and", num2, "is:", multiplication_result)
print("Division of", num1, "by", num2, "is:", division_result)
