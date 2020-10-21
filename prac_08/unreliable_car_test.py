"""Test UnreliableCar class."""

from prac_08.unreliable_car import UnreliableCar

def main():

    # Test __init__
    good_car = UnreliableCar("Good", 100, 90)
    bad_car = UnreliableCar("Bad", 100, 10)
    print(good_car)
    print(bad_car)

    # Test drive
    for i in range(1, 12):
        print("Try to drive {}km".format(i))
        print("{} drove {}km)".format(good_car.name, good_car.drive(i)))
        print("{} drove {}km)".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)



main()