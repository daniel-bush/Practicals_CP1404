"""Practice - car simulator CP1404."""

from prac_06.car import Car

MENU = "Menu:\n" \
       "d) drive\n" \
       "r) refuel\n" \
       "q) quit\n" \
       "Enter your choice: "


def main():
    """Main code to drive a car looking at the fuel, the odo and distance."""
    print("Let's drive!")
    car_name = input("Enter the name of your car: ")
    car = Car(car_name, 100)
    menu_choice = ""
    while menu_choice != "Q":
        menu_choice = load_menu(car)
        if menu_choice == "D":
            car = drive_car(car)
        elif menu_choice == "R":
            car = refuel_car(car)
    print("\nGoodbye {}'s driver.".format(car.name))


def load_menu(car):
    """Loads the main menu - checks for errors and returns the selected option."""
    print("\n{}".format(car))
    menu_choice = input(MENU).upper()
    while menu_choice not in ["D", "R", "Q"]:
        print("Invalid choice\n")
        print(car)
        menu_choice = input(MENU).upper()
    return menu_choice


def refuel_car(car):
    "Function to refuel car."
    fuel = check_valid_number("How many units of fuel do you want to add to the car? ", "Fuel amount")
    car.add_fuel(fuel)
    print("Added {} units of fuel.".format(fuel))
    return car


def drive_car(car):
    """Function to drive the car a certain distance."""
    required_distance = check_valid_number("How many km do you wish to drive: ", "Distance")
    distance_traveled = car.drive(required_distance)
    if car.fuel != 0:
        print("The car drove {}km.".format(distance_traveled))
    else:
        print("The car drove {}km and ran out of fuel.".format(distance_traveled))
    return car


def check_valid_number(message, unit):
    """Checks if the number is valid. >= 0 is only accepted."""
    valid_number = False
    while not valid_number:
        try:
            number = float(input(message))
            if number >= 0:
                valid_number = True
            else:
                print("{} must be >= 0".format(unit))
        except ValueError:
            print("Please insert a valid number!")
    return number


main()
