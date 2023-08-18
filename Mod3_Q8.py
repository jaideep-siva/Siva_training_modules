"""
Module 3 Q9 

Description: This program determines if the sum of two numbers is odd or even

Author: Jaideep Siva Sen


"""

# Asking for inputs
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

"""
 determining odd or even
 if a number is moduls by two equals zero it means it's even else it's odd
"""
if (num_1 + num_2) % 2 == 0:
    print("Even")

else:
    print("Odd")


