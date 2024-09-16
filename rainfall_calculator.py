# Program to calculate average rainfall over a period of years

# Get the number of years from the user
num_years = int(input("Enter the number of years: "))

# Initialize variables
total_rainfall = 0.0
total_months = 0

# Outer loop for each year
for year in range(1, num_years + 1):
    print(f"\nYear {year}")

    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Display the results
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
