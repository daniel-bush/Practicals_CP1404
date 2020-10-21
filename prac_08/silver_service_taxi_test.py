"""Test SilverServiceTaxi class."""

from prac_08.silver_service_taxi import SilverServiceTaxi

def main():

    # test init

    fancy_taxi = SilverServiceTaxi("Very Fancy", 100, 10)
    less_fancy_taxi = SilverServiceTaxi("Less Fancy", 100, 3)
    normal_taxi = SilverServiceTaxi("Normal Taxi", 100, 1)

    print()


main()