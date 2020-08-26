"""
CP1404/CP5632 - Practical
Conversion between celsius and fahrenheit calculator
"""

MENU = "C - Convert Celsius to Fahrenheit\n" \
       "F - Convert Fahrenheit to Celsius\n" \
       "Q - Quit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(result))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(result))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
