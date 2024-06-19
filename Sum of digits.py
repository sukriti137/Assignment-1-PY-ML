def sum_of_digits(number):
    # Convert number to positive integer (in case it's negative)
    number = abs(number)
    
    # Initialize sum to zero
    total_sum = 0
    
    # Iterate over each digit in the number
    while number > 0:
        # Extract the last digit using modulo operation
        digit = number % 10
        
        # Add the digit to the total sum
        total_sum += digit
        
        # Remove the last digit from the number
        number = number // 10
    
    return total_sum

# Example usage:
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"Sum of digits of {number} is: {result}")
