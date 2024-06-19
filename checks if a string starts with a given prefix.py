def starts_or_ends_with(string, prefix=None, suffix=None):
    starts_with_prefix = False
    ends_with_suffix = False

    if prefix is not None:
        starts_with_prefix = string.startswith(prefix)
    
    if suffix is not None:
        ends_with_suffix = string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

# Example usage:
s = "Hello, world!"
prefix_to_check = "Hello"
suffix_to_check = "world!"

starts_with, ends_with = starts_or_ends_with(s, prefix_to_check, suffix_to_check)

print(f'Starts with "{prefix_to_check}": {starts_with}')
print(f'Ends with "{suffix_to_check}": {ends_with}')
