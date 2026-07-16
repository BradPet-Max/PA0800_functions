#Question 1 -Create a function called calculateArea.
def calculateArea(length, width):
    area = length * width
    print(area)

calculateArea(10, 5)

#Question 2-Create a function called calculateSalary.
def calculateSalary(basicSalary, bonus):
    totalSalary = basicSalary + bonus
    print(totalSalary)

calculateSalary(15000, 2500)

#Question 3 -Explain why internal variables cannot be accessed outside the function.
#nternal variables (also called local variables) only exist inside the function where they are created.
# Once the function finishes running, those variables are destroyed and cannot be accessed from outside the function. 
# This helps prevent accidental changes to the variables and keeps the code organized.

#Question 4 -What would happen if two different functions both used a global variable with the same name?
#If two different functions use the same global variable, they share the same value. 
# If one function changes the variable, the other function will see the updated value. 
# This can lead to unexpected results or bugs, so it is generally better to use local variables whenever possible.