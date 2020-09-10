"""Practice - car simulator CP1404."""

from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter the name of your car: ")
    car = Car(car_name, 100)
    # drive
    car = drive_car(car)


def drive_car(car):
    required_distance = check_valid_number("How many km do you wish to drive: ")
    distance_traveled = car.drive(required_distance)
    if car.fuel != 0:
        print("The car drove {}km.".format(distance_traveled))
    else:
        print("The car drove {}km and ran out of fuel.".format(distance_traveled))
    return car


def check_valid_number(message):
    valid_number = False
    while not valid_number:
        try:
            number = float(input(message))
            if number >= 0:
                valid_number = True
            else:
                print("Distance must be >= 0")
        except ValueError:
            print("Please insert a valid number!")
    return number


main()
