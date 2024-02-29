# Creating a program where you enter a positive integer
# Run a loop with calculation and it will keep calculating new values
# If the output is an even number divide by 2
# Else, multiply it by three and add one

number = int(input("Please enter a number "))

while number != 1:
    if (number % 2) == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)



