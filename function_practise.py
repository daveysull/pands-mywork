# Task1 : Write a function that takes two numbers as input and returns their sum.
'''
def add_numbers(num1, num2):
    return num1+num2

result = add_numbers(5,3)
print(result)


# Task 2: Write a function that takes a list of numbers as input and returns the average of those numbers.


# First define the function and what will be put into it ie values
# * Means that the function can accept any number of arguments and will be packed into the tuple name values

# Start off simple, what do we want the function to achieve and what do we need to do that
# We need the number of values which we achieve with the len function
# And we need the sum of the values
# Don't forget to flag what you want returned

def ave (*values):
    length = len(values)
    sum = 0 
    for value in values:
        sum += value
    average = sum / length
    return average

print(ave(1,2,3,4,5))


# Task No.3 Write a function that takes a string as input and returns the reverse of that string
# Use the negative step in slicing

def reverse (name):
    return name [::-1]

print(reverse("dave"))
'''

# Task 4 : Write a function that takes a list of integers as input and returns a new list containing 
# only the even numbers from the original list.

# Break it down, what do we want the function to achieve and what do we need.
# A number is even if it can be divided by 2, potentially an if statement here?

def even(*values):
    for value in values:
        if value % 2 == 0:
            print(value)

print(even(1,2,3,4,5,6,7,8,9))