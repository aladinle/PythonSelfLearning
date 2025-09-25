# Challenges (Day 2):

# Find largest of 3 numbers.
def largestOf3():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("Enter third number: ")  
    return max(a, b, c)
    # if(a >= b and a >= c):
    #     return a
    # elif(b >= a and b >= c):
    #     return b
    # else:
    #     return c

# Check if year is leap year.
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False

# Print multiplication table of a number.

# Sum of numbers 1 to 100
def sum1to100():
    total = 0
    return sum(range(1,101))

# Reverse a number.
def reverseNumber():
    n = input("Enter a number to reverse: ")
    return n[::-1]

# Count digits in a number.
def countDigits():
    n = input("Enter a number to count digits: ")
    return len(str(n))

# Guess-the-number game (random.randint)
import random
def guessTheNumber():
    input("*** Press Enter to start the game *** ")
    random_number = random.randint(1, 100)
    while True:
        user_guess = int(input("Enter your guess from 1 - 100: "))
        if user_guess == random_number:
            print("You guessed it right!")
            break
        elif user_guess < random_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

# Print Fibonacci series up to n.
def fibonacci():
    n =  int(input("Enter a number to generate Fibonacci series up to: "))
    a, b = 0, 1
    series = []
    while a < n:
        series.append(a)
        a, b = b, a + b
    print(series)

# Print all prime numbers up to 100.
def primesUpTo100():
    n = int(input("Enter a number to print all prime numbers up to: "))
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1): # Check divisibility up to square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(primes)

# Calculate factorial of a number (loop).
# Solution 1 (iterative)
# def factorial(n):
#     factorial = 1
#     if n <= 0:
#         return "Factorial not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print(factorial)

# Solution 2 (recursive)
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    


def main(): 
    maxOf3 = largestOf3()
    print(f"Largest of 3 numbers is: {maxOf3}")
    year = int(input("Enter year to check if leap year: "))
    print(f"Check if {year} is leap year: {isLeapYear(year)}")
    print(f"Sum of numbers from 1 to 100 is: {sum1to100()}")
    print(f"Reversed number is: {reverseNumber()}")
    print(f"Count of digits is: {countDigits()}")
    guessTheNumber()    
    fibonacci()
    primesUpTo100()
    n = int(input("Enter a number to calculate factorial: "))
    print(factorial(n))

if __name__ == "__main__":
    main()
