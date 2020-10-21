"""Test UnreliableCar class."""

from prac_08.unreliable_car import UnreliableCar

def main():

    # Test __init__
    good_car = UnreliableCar("Good", 100, 90)
    bad_car = UnreliableCar("Bad", 100, 10)
    print(good_car)
    print(bad_car)


main()