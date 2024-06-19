def find_min_max(numbers):
    # Return a tuple containing the minimum and maximum values
    return min(numbers), max(numbers)

# Example list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Find the minimum and maximum values
min_value, max_value = find_min_max(numbers)

# Print the results
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
