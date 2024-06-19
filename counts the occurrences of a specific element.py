def count_occurrences(lst, element):
    return lst.count(element)

# Example list and element to count
example_list = [1, 2, 3, 4, 2, 2, 5, 2, 3]
element_to_count = 2

# Count the occurrences
occurrences = count_occurrences(example_list, element_to_count)

# Print the result
print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")
