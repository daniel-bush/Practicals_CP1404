"""Taxi simulator."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive\n" \
       ">>>"

def main():
    """This program simulates a taxi service company."""

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    print("Let's drive!")
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_validated_taxi_number(taxis)
        elif menu_choice == "d":
            pass
        else:
            print("invalid choice")
        menu_choice = input(MENU).lower()


def display_taxis(taxis):
    for taxi in enumerate(taxis, 1):
        print("{} - {}".format(taxi[0], taxi[1]))


def get_validated_taxi_number(taxis):
    number_of_taxis = len(taxis)
    number_valid = False
    while not number_valid:
        try:
            taxi_number = int(input("Choose Taxi: "))
            if taxi_number < 1 or taxi_number > number_of_taxis:
                print("Please select correct taxi number.")
            else:
                number_valid = True
        except ValueError:
            print("Incorrect value. Please enter number.")
    return taxi_number-1












main()

