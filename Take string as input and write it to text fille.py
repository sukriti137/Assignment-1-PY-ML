def main():
    # Get input string from user
    input_string = input("Enter a string to write to a file: ")
    
    # Ask user for the file name to write to
    filename = input("Enter the filename to write to (include extension, e.g., 'output.txt'): ")
    
    # Write the input string to the file
    try:
        with open(filename, 'w') as file:
            file.write(input_string)
        print(f'Successfully wrote the string "{input_string}" to {filename}')
    except IOError:
        print(f'Error writing to {filename}')

if __name__ == "__main__":
    main()
