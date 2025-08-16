def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Ask the user for input
original_price = float(input("Enter the original price of an item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount)

# Print the final price
print("Your final price is: $" + str(final_price))