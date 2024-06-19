import string

def remove_punctuation(input_string):
    # Create a translation table that maps punctuation characters to None
    translator = str.maketrans('', '', string.punctuation)
    # Translate the input string using the translation table
    cleaned_string = input_string.translate(translator)
    return cleaned_string

# Input string
input_string = "Hello, world! This is a test string with punctuation: should be removed."

# Remove punctuation
cleaned_string = remove_punctuation(input_string)

# Print the result
print(cleaned_string)
