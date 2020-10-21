"""Taxi simulator."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive\n" \
       ">>>"

def main():
    """This program simulates a taxi service company."""

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            pass
        elif menu_choice == "d":
            pass
        else:
            print("invalid choice")
        menu_choice = input(MENU).lower()



main()

