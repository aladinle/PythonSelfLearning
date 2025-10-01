# Learn:

# Define functions (def)

# Arguments, return values

# Recursion

# Importing built-in modules (math, random, datetime)

# Challenges (Day 4):

# Function to check prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to calculate factorial (recursion).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to generate Fibonacci series.
def fibonacci(n):
    fib_series = []
    a,b = 0,1
    for _ in range (n):
        fib_series.append(a)
        a,b = b, a + b
    return fib_series

# Function to check Armstrong number.
# 153 is Amstrong number
# It has 3 digits → power = 3
# 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 153 `
def is_armstrong(num):
    # check how many digits
    digits = len(str(num))
    sum_of_powers = sum(int(digit) ** digits for digit in str(num))
    return sum_of_powers == num

# Function to reverse a string.
def reverse_string(s):
    return s[::-1]

# Function to count vowels in a string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    # sum = 0
    # for c in s:
    #     if c in vowels:
    #         sum += 1
    # return sum
    return sum(1 for c in s if c in vowels) # 1 line version


# Function to check if string is palindrome.
def is_palindrome(s):
    return s == s[::-1]

# Function to find GCD of two numbers.
import math
# def gcd(a, b):
#     return math.gcd(a,b)
def gcd(a, b):
    while b:
        a,b = b, a % b
    return a

# Use math to find square root, power, log.
def math_operations(num):
    sqrt_val = math.sqrt(num)
    power_val = math.pow(num, 2)  # num squared
    log_val = math.log(num) if num > 0 else None  # natural log
    return sqrt_val, power_val, log_val

# Build a dice roller using random.randint.
import random
def roll_dice():
    return random.randint(1, 6)


def main():
    num1 = int(input("Enter a number to check Prime: "))
    print(f"{num1} is Prime" if is_prime(num1) else f"{num1} is not Prime")
    num2 = int(input("Enter a number to calculate Factorial: "))
    print(f"Factorial of {num2} is {factorial(num2)}")
    num3 = int(input("Enter how many Fibonacci numbers to generate: "))
    print(f"Fibonacci series of {num3} numbers: {fibonacci(num3)}")
    num4 = int(input("Enter a number to check Armstrong: "))
    print(f"{num4} is Armstrong" if is_armstrong(num4) else f"{num4} is not Armstrong")
    str1 = input("Enter a string to reverse: ")
    print(f"Reversed string: {reverse_string(str1)}")
    str2 = input("Enter a string to count Vowels: ")
    print(f"Number of vowels in '{str2}': {count_vowels(str2)}")
    str3 = input("Enter a string to check Palindrome: ")
    print(f"{str3} is Palindrome" if is_palindrome(str3) else f"{str3} is not Palindrome")
    num5 = int(input("Enter first number to find GCD: "))
    num6 = int(input("Enter second number to find GCD: "))
    print(f"GCD of {num5} and {num6} is {gcd(num5, num6)}")
    num7 = int(input("Enter a number for math operations (sqrt, power, log): "))
    sqrt_val, power_val, log_val = math_operations(num7)
    print(f"Square root: {sqrt_val}, Power (squared): {power_val}, Log: {log_val}")
    print(f"Dice rolled: {roll_dice()}")
    
if __name__ == "__main__":
    main()