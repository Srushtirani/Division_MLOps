# Write a Python program to accept two numbers and display its division.

num = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))

if num < denominator:
    result = num / denominator
    print("Division =", result)
    print("Numerator is less than denominator.")
else:

    if denominator != 0:
        result = num / denominator
        print("Division =", result)
    else:
        print("Division by zero is not allowed.")
        