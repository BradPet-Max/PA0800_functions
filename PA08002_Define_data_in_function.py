#Question 1-Create a function called welcome that takes one parameter city and prints:
def welcome(city):
    print(f"Welcome to {city}")

welcome("Cape Town")

#Question 2-Create a function that takes two numbers and prints their difference.
def difference(num1, num2):
    print(num1 - num2)

difference(20, 8)

#Question 3-Create a function called introduce that takes two parameters:
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")

introduce("Peter", 35)

#Question 4 -Explain the difference between a parameter and an argument.
#A parameter is a variable listed in a function's definition. It acts as a placeholder for the value the function will receive.
#An argument is the actual value that is passed to the function when it is called.

def welcome(city):      # city is a parameter
    print(f"Welcome to {city}")

welcome("Cape Town")    # "Cape Town" is an argument