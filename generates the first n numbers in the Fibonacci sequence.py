def fibonacci_sequence(n):
    # List to store the Fibonacci sequence
    fib_sequence = []
    
    # Check if n is a valid number
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Starting values for the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Input: Number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Output: Fibonacci sequence
print(fibonacci_sequence(n))
