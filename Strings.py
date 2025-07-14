#1. Print All Duplicate Characters in a String

def print_duplicates(string):
    char_count = {}
    for char in string:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1
    print("Duplicate characters:")
    for char, count in char_count.items():
        if count > 1:
            print(f"'{char}' appears {count} times")
input_str = "programming language"
print_duplicates(input_str)

#2. Replace Vowels with ‘*’

def replace_vowels_with_star(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result
input_str = "Happy Birthday to you"
output_str = replace_vowels_with_star(input_str)
print("Original String:", input_str)
print("Modified String:", output_str)

#3. Convert a Snake_Case String to CamelCase.

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case
input_str = "convert_this_string_to_camelcase"
output_str = snake_to_camel(input_str)
print(output_str)

#4. Use reduce() to Find Product of List Elements

from functools import reduce
numbers = [2, 3, 4, 5, 6]
product = reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)