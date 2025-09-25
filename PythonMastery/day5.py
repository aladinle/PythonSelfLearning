# Learn:

# File handling (open, read, write, with)

# Exceptions (try, except, finally)

# List comprehensions

# Lambda functions, map, filter, reduce

# Challenges (Day 5):

# Write names to a file, then read them back.
import os
from token import OP
def read_write_file(filename, names):
    # check if file exists
    with open(filename, 'w') as f:
        for name in names:
            f.write(name + '\n')
    with open(filename, 'r') as f:
        return f.readlines() 

# Count words in a file.
# def count_words_in_file(filename):
#     with open(filename, 'r') as f:
#         # read entire file content
#         text = f.read()
#         # split by whitespace to get words
#         words = text.split()
#         # return word count
#         return len(words)
from collections import Counter
def count_words_in_file(filename):
    with open(filename, 'r') as f:
        counts = Counter(f.read().split()) # counts = {'Alice': 1, 'Bob': 1, 'Charlie': 1}}
    return sum(counts.values())

# Append text to an existing file.
def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')
    with open(filename, 'r') as f:
        return f.readlines()

# Handle division by zero error.
def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # clean up actions if any
        pass

# Create list comprehension => squares of numbers 1–10.
def squares_list():
    return [x**2 for x in range(1,11)]

# Filter even numbers from a list using filter.
def filter_even_numbers(numbers):
    return list(filter(lambda x: x%2==0, numbers))

# Use map to convert list of strings to uppercase.
def uppercase_list(strings):
    return list(map(lambda s: s.upper(), strings))

# Use reduce to find product of list numbers.
from functools import reduce
def product_of_list(numbers):
    return reduce(lambda x,y: x*y, numbers)

# # Given [100, 50, 25], use reduce to compute their GCD.
# def gcd(numbers):
#     return reduce(lambda x,y: x if y == 0 else gcd([y,x %y]), numbers)

# # From [5, 3, 9, 1, 6], use reduce to find the maximum number.
# def max_in_list(numbers):
#     return reduce(lambda x,y: x if x > y else y, numbers)

# Count vowels in a file.
def count_vowels_in_file(filename):
    vowels = 'aeiouAEIOU'
    count = 0
    # with open(filename, 'r') as f:
    #     text = f.read()
    #     for char in text:
    #         if char in vowels:
    #             count += 1
    # return count

    with open(filename, 'r') as f:
        return sum(1 for char in f.read() if char in vowels)

# Read a CSV file line by line (csv module).
import csv
def read_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def main():
    #1 Write names to a file, then read them back.
    filename = 'names.txt'
    names = ['Alice', 'Bob', 'Charlie']
    lines = read_write_file(filename, names)
    print("Names in file:")
    for line in lines:
        print(line.strip())
    # # Clean up
    # os.remove(filename)   # remove names.txt after reading

    # 2 Count words in a file.
    print(f"\nWord count in this file: {count_words_in_file(filename)}")

    # 3 Append text to an existing file.
    append_text = "David"
    append_to_file(filename, append_text)
    print("\nAfter appending:")
    lines = read_write_file(filename, names + [append_text])
    for line in lines:
        print(line.strip())

    # 4 Handle division by zero error.
    print("\nSafe division:")
    print(safe_divide(10, 2))  # Should print 5.0
    print(safe_divide(10, 0))  # Should handle division by zero
    print(safe_divide(10, 'a'))  # Should handle other exceptions

    # 5 Create list comprehension => squares of numbers 1–10.
    print("\nSquares of numbers 1-10:")
    print(squares_list())

    # 6 Filter even numbers from a list using filter.
    numbers = list(range(1, 21))
    print("\nEven numbers from 1 to 20:")
    print(filter_even_numbers(numbers))

    # 7 Use map to convert list of strings to uppercase.
    strings = ['hello', 'world', 'python']
    print("\nUppercase strings:")
    print(uppercase_list(strings))

    # 8 Use reduce to find product of list numbers.
    nums = [1, 2, 3, 4]
    print("\nProduct of list numbers [1,2,3,4]:")
    print(product_of_list(nums))

    # 9 Count vowels in a file.
    print(f"\nVowel count in this file: {count_vowels_in_file(filename)}")

    # 10 Read a CSV file line by line (csv module).
    csv_filename = 'sample.csv'
    # Create a sample CSV file for demonstration
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', 30, 'New York'])
        writer.writerow(['Bob', 25, 'Los Angeles'])
    # read and print CSV content
    with open(csv_filename, 'r') as f:
        print("\nCSV file content:")
        csv_content = read_csv_file(csv_filename)
        for row in csv_content:
            print(row)

    # # 11 gcd of [100, 50, 25]
    # nums_for_gcd = [100, 50, 25]
    # print(f"\nGCD of {nums_for_gcd}: {gcd(nums_for_gcd)}")

    # # 12 max in [5, 3, 9, 1, 6]
    # nums_for_max = [5, 3, 9, 1, 6]
    # print(f"\nMax in {nums_for_max}: {max_in_list(nums_for_max)}")

if __name__ == "__main__":
    main()
