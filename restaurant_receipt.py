
# Take food price as input
food_price = float(input("Enter the food price: $"))

tip_rate = 0.18  # 18%
sales_tax_rate = 0.07  # 7%

# Calculate tip and sales tax
tip = food_price * tip_rate
sales_tax = food_price * sales_tax_rate

# Calculate the total amount
total = food_price + tip + sales_tax

# Print receipt
print(f"Food price: ${food_price:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales tax (7%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
