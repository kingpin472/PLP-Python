def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Only applies discount if it is 20% or higher.
    
    Parameters:
    - price (float): The original price
    - discount_percent (float): Discount percentage

    Returns:
    - float: Final price after discount or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate and display final price
    final_price = calculate_discount(original_price, discount)

    if final_price < original_price:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values.")
