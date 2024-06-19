def main():
    # Ask user for the file name to read from
    filename = input("Enter the filename to read from (include extension, e.g., 'input.txt'): ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f'Content of {filename}:')
            print(content)
    except FileNotFoundError:
        print(f'Error: File {filename} not found.')
    except IOError:
        print(f'Error reading from {filename}.')

if __name__ == "__main__":
    main()
