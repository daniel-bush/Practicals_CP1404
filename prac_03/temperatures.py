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
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32



main()
