def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator!"

def main():
    print("Welcome to the Simple Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    
    result = calculate(num1, num2, operator)
    
    # Check if result is a float with no fractional part and convert it to int if so
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
