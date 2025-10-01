#Print "Hello, Python!"
def printHello():
    print("Hello, Python!\n")
    
#Swap two numbers without using a third variable.
def swap2numbers(first, second):        # 5, 10 => need 10, 5
    print(f'Before swap: {first}, {second}')
    first = first + second              # first = 5 + 10 = 15, second = 10
    second = first - second             # second = 15 - 10 = 5
    first = first - second              # first = 15 - 5 = 10
    print(f'After swap: {first}, {second}')

#Take user input for name & age → print: "Hello NAME, you are AGE years old."
def inputInfo():
    name = input("Enter name: ")
    age = input("Enter age: ")
    print(f"Hello {name}, you are {age} years old.")

#Convert Celsius to Fahrenheit.
def convertCtoF():
    celsius = float(input("Enter celsius: "))
    print(f"Celsius: {celsius}")
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Fahrenheit: {fahrenheit}")

#Calculate area of a circle from radius.
def areaOfCircle():
    radius = float(input("Enter radius of circle: "))
    area = 3.14159 * radius * radius
    print(f"Area of circle with radius {radius} is {area}")

#Find simple interest.
def simpleInterest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    interest = (principal * rate * time) / 100
    print(f"Simple Interest is: {interest}")

#Check if a number is even or odd.
def checkEvenOdd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

#Find square and cube of a number.
def squareAndCube():
    number = float(input("Enter a number: "))
    square = number ** 2
    cube = number ** 3
    print(f"Square of {number} is {square}")
    print(f"Cube of {number} is {cube}")

#Take two numbers and print their sum, difference, product, quotient.
def sumDiffProdQuot(a, b):
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    if b != 0:
        print(f"Quotient: {a / b}")
    else:
        print("Quotient: Division by zero is not allowed.")

#Check type of different variables (type()).
def checkVariableTypes(val):
    print(f"The type of the variable is: {type(val)}")

def main():
    print("***************************")
    print("Question 1:")
    printHello()
    print("***************************")
    print("Question 2:")
    swap2numbers(5,10)
    print("***************************")
    print("Question 3:")
    inputInfo()
    print("***************************")
    print("Question 4:")
    convertCtoF()
    print("***************************")
    print("Question 5:")
    areaOfCircle()
    print("***************************")
    print("Question 6:")
    simpleInterest()
    print("***************************")
    print("Question 7:")
    checkEvenOdd()
    print("***************************")   
    print("Question 8:")
    squareAndCube()
    print("***************************")   
    print("Question 9:")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    sumDiffProdQuot(a, b)
    print("***************************")   
    print("Question 10:")
    val = {1,2,3}
    checkVariableTypes(val)

if __name__ == "__main__":
    main()