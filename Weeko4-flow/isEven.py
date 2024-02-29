#Write a program that asks the user to enter a number and the program will tell us if it's odd or even

number = int(input("Enter a number.. "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
