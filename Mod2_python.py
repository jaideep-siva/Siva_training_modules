if __name__ == "__main__":
"""
Obtaining 4 values from user  to calculate and output average
"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    # adding the 4 values and dividing by 4 to calculate average 
    average = (num1 + num2 + num3 + num4) / 4

    #Ouputing average as a float with hundreths accuracy
    print(f"The average of {num1}, {num2}, {num3}, and {num4} is: {average:.2f}")
