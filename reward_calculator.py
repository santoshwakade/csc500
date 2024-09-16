# Program to calculate points awarded based on books purchased

# Get the number of books purchased from the user
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine the points awarded based on the number of books
if books_purchased >= 8:
    points = 60
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 2:
    points = 5
elif books_purchased == 0:
    points = 0
else:
    points = 0  # In case the number of books is less than zero

# Display the points awarded
print(f"You have been awarded {points} points for purchasing {books_purchased} books.")
