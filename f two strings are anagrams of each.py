def are_anagrams(string1, string2):
    # Remove any whitespace and convert strings to lowercase
    cleaned_string1 = ''.join(string1.split()).lower()
    cleaned_string2 = ''.join(string2.split()).lower()
    
    # Sort the characters of both strings
    sorted_string1 = sorted(cleaned_string1)
    sorted_string2 = sorted(cleaned_string2)
    
    # Check if the sorted characters are the same
    return sorted_string1 == sorted_string2

# Input strings
string1 = "listen"
string2 = "silent"

# Check if the strings are anagrams
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
