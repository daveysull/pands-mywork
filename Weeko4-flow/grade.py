# Write a program (grade.py) that reads in a student’s percentage mark and prints out corresponding the grade (the program should check that the percentage is valid: 
#•  Under 40% => Fail • Between 40% and 49%  => Pass 
#• Between 50% and 59%  => Merit 2 
#• Between 60% and 69%  => Merit 1 
#• Over 70%    => Distinction 

import math 

percentage = float(input("Enter the percentage: "))
percentage = math.ceil(percentage)

if percentage < 0 or percentage > 100:
    print("Please enter number between 0 and 100")
elif percentage < 40:
    print("fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit2")
elif percentage < 70:
    print("Merit1")
else:
    print("Distinction")
    
