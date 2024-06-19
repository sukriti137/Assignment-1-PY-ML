def main():
    # Get input strings from user
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check for: ")
    
    # Check if substring is present in the main string
    if substring in main_string:
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is NOT present in the main string.")

if __name__ == "__main__":
    main()
