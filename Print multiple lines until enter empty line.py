def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

if __name__ == "__main__":
    print("Enter multiple lines of text. Press Enter on an empty line to finish.")
    lines = read_lines_until_empty()
    
    if lines:
        print("\nEntered lines:")
        for line in lines:
            print(line)
    else:
        print("No lines entered.")
