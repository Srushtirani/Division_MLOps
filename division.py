#Write a Python program to accept two numbers and display its division.
#num = float(input("Enter numerator: "))
#denominator = float(input("Enter denominator: "))

#if num < denominator:
 #   print("Numerator is less than denominator.")
#else:
#    if denominator != 0:
  ##      result = num / denominator
   #     print("Division =", result)
   # else:
    #    print("Division by zero is not allowed.")
        

def divide_numbers(num, denominator):

    if denominator == 0:
        raise ValueError("Division by zero is not allowed")

    if num < denominator:
        print("Numerator is smaller than denominator")

    return num / denominator


if __name__ == "__main__":
    num = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    try:
        result = divide_numbers(num, denominator)
        print("Division =", result)

    except ValueError as e:
        print("Error:", e)
