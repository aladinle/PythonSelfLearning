# Learn:

# Lists, Tuples, Sets, Dictionaries
# Lists:
#     Ordered, Mutable, Allows Duplicates
#     Created with [] or list()
#     Supports indexing, slicing, CRUD (Create, Read, Update, Delete)
# Tuples:
#     Ordered, Immutable, Allows Duplicates
#     Created with () or tuple()
#     Supports indexing, slicing, Read-only
#     Useful for fixed collections (e.g., coordinates)
# Sets:
#     Unordered, Mutable, No Duplicates
#     Created with {} or set()
#     Supports mathematical set operations (union |, intersection &)
#     Useful for membership testing, removing duplicates
# Dictionaries:
#     Unordered, Mutable, Key-Value pairs
#     Created with {} or dict()

# Indexing, slicing
# Indexing: Access elements by position (0-based, works on list, tuple, string)
# Slicing: Extract sub-parts using [start:stop:step] (works on list, tuple, string)

# CRUD operations on lists
# Create: append(), insert(), extend()
# Read: indexing, slicing, iteration
# Update: assign by index, slice assignment
# Delete: del, remove(), pop(), clear()

# Iterating collections
# for loop, while loop, list comprehensions
#==========================================================================
# Challenges (Day 3):

# Create a list of 10 numbers → find max & min.
from operator import le, ne
import random
from re import L, M, S
from turtle import left
def find_max_min():
#    numbers = []
    numbers = list()
    for i in range(10):
        numbers.append(random.randint(1,100))
    return (max(numbers), min(numbers))

# Reverse a list without reverse() or slicing.
# Solution 1: Using a loop to insert elements at the beginning of a new list.
# Works fine but infficient (O(n^2)) due to insert(0, item) operation.
# def reverse_list(lst):
#     reversed_lst = []
#     for item in lst:
#         reversed_lst.insert(0, item)
#     return reversed_lst

# Solution 2: Better approach using two-pointer technique.
# Time complexity O(n).
# In-place reversal. Space complexity O(1).
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Remove duplicates from a list.
# Solution 1: Using a new list to store unique elements.
# Time complexity O(n^2) due to 'in' check in list for worst case.
# def remove_duplicates():
#     org_lst = [1,2,2,3,4,4,5]
#     unique_lst = []
#     for item in org_lst:
#         if item not in unique_lst:
#             unique_lst.append(item)
#     return unique_lst

# Solution 2: use built-in dict.fromkeys() to remove duplicates while preserving order.
# dict.fromkeys() automatically removes duplicates because dictionary keys are unique.
# More Pythonic & Faster Approaches
# Time complexity O(n).
# def remove_duplicates():
#     org_lst = [1,2,2,3,4,4,5]
#     return list(dict.fromkeys(org_lst))

# Solution 3: Using set()
# Time complexity O(n), keep order, very compact.
def remove_duplicates():
    org_lst = [1,2,2,3,4,4,5]
    seen = set()
    return [x for x in org_lst if not (x in seen or seen.add(x))]


# Sort a list without using sort().
# Solution: Implementing bubble sort.
# Time complexity O(n^2) - inefficient for large lists.
# Space complexity O(1) - in-place sorting.
# def sort_list():
#     lst = [5,3,1,4,2]
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     return lst
# Solution 2: Using merge sort (more efficient).
# Time complexity O(n log n).
# support function to merge two sorted lists 
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)
  
# call merger_sort   
def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Count frequency of elements in a list.
# Solution 1: Using a dictionary to count occurrences.
# Time: O(n) — single loop, dictionary operations are O(1) average.
# Space: O(k) — dictionary storing frequencies, where k = number of unique element
# def count_frequency():
#     lst = [1,2,2,3,4,4,4,5]
#     frequencys = {}
#     for item in lst:
#         if item in frequencys:
#             frequencys[item] += 1
#         else:
#             frequencys[item] = 1
#     return frequencys
# Solution 2: Using collections.Counter for simplicity and efficiency.
# Time: O(n)
# Space: O(k)
from collections import Counter
def count_frequency():
    lst = [1,2,2,3,4,4,4,5]
    return dict(Counter(lst))

# Merge two lists and remove duplicates.
# Solution 1: Using set to remove duplicates.
# Time complexity O(n + m) due to set operations.
# Space complexity O(n + m) for the merged list and set.
# def merge_lists_remove_duplicates():
#     list1 = [1,2,3]
#     list2 = [3,4,5]
#     seen = set()
#     merged_list = list1 + list2
#     unique_list = []
#     for item in merged_list:
#         if item not in seen:
#             seen.add(item)
#             unique_list.append(item)
#     return unique_list
# Solution 2: Using dict.fromkeys() to remove duplicates while preserving order.
# Time complexity O(n + m).
# Space complexity O(n + m).
def merge_lists_remove_duplicates():
    list1 = [1,2,3]
    list2 = [3,4,5]
    return list(dict.fromkeys(list1 + list2))
# Solution 3: using union set() to remove duplicates.
# def merge_lists_remove_duplicates():
#     list1 = [1,2,3]
#     list2 = [3,4,5]
#     return list(set(list1) | set(list2))

# Access nested dictionary values.
# Create a dictionary for student names & marks.
def access_nested_dict():
    nested_dict = {
        'student1': {'name': 'Alice', 'marks': 85},
        'student2': {'name': 'Bob', 'marks': 90},
        'student3': {'name': 'Joe', 'marks': 95},
    }
    print(f"Accessing nested dictionary values:{nested_dict['student1']['name']}, {nested_dict['student2']['marks']}, {nested_dict['student3']['marks']}")
#     for key,value in nested_dict.items():
#         print(f"{key}: {value}")

# Find union & intersection of two sets.
def set_operations():
    set1 = {1,2,3,4}
    set2 = {3,4,5,6}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")

# Check if a word is palindrome using list.
def is_palindrome(word):
    return word == word[::-1]

def main(): 
    max, min = find_max_min()
    print(f"Max: {max}, Min: {min}")
    lst = [1, 2, 3, 4, 5]
    print(f"Original List: {lst}")
    print(f"Reversed List: {reverse_list(lst)}")
    print(f"List after removing duplicates: {remove_duplicates()}")
    print(f"Frequency count: {count_frequency()}")
    #print(f"Sorted List: {sort_list()}")
    lst = [5,3,1,4,2]
    print(f"Sorted List using merge sort: {merge_sort(lst)}")
    merge_lists_remove_duplicates()
    print(f"Merged List without duplicates: {merge_lists_remove_duplicates()}")
    access_nested_dict()
    set_operations()
    word = input("Enter a word to check if it's a palindrome: ")
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
    
if __name__ == "__main__": 
    main()
