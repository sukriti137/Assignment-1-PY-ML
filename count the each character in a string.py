def count_character_frequency(input_string):
    # Create an empty dictionary to store the frequency of each character
    frequency_dict = {}

    # Iterate over each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

# Input string
input_string = "example string to count character frequency"

# Count the frequency of each character
frequency = count_character_frequency(input_string)

# Print the frequency of each character
for char, count in frequency.items():
    print(f"'{char}': {count}")
