def string_to_list_of_characters(input_string):
    # Using list comprehension to convert string to list of characters
    characters_list = [char for char in input_string]
    return characters_list

# Example usage:
input_string = "Hello, world!"
characters_list = string_to_list_of_characters(input_string)

print(f"Original string: {input_string}")
print(f"List of characters: {characters_list}")
