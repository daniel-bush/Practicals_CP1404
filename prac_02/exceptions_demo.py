"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

# When anything other than an integer is entered.

2. When will a ZeroDivisionError occur?

# if a zero value is entered for the domoninator - can't divid by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

# yes see below

"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator can not equal zero!\nEnter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# this will never happen
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")