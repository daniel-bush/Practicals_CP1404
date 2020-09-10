"""Practice - car simulator CP1404."""

from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter the name of your car: ")
    car = Car(car_name, 100)

    # drive
    distance = check_valid_number("How many km do you wish to drive: ")


def check_valid_number(message):
    valid_number = False
    while not valid_number:
        try:
            number = float(input(message))
            if number >= 0:
                valid_number = True
            else:
                print("Number must be 0 or higher!")
        except ValueError:
            print("Please insert a valid number!")
    return number


main()
