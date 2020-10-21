"""Test SilverServiceTaxi class."""

from prac_08.silver_service_taxi import SilverServiceTaxi

def main():

    # test init

    fancy_taxi = SilverServiceTaxi("Very Fancy", 100, 10)
    less_fancy_taxi = SilverServiceTaxi("Less Fancy", 100, 3)
    normal_taxi = SilverServiceTaxi("Normal Taxi", 100, 1)

    print(fancy_taxi)
    print(less_fancy_taxi)
    print(normal_taxi)

    # test flagfall

    print(fancy_taxi.flagfall)

    # test get_fare

    fancy_taxi.drive(50)
    expected_fare = (50*1.23*10+4.5)
    actual_fare = fancy_taxi.get_fare()
    print("expected fare = {}, actual fare = {}".format(expected_fare, actual_fare))

    # test __str__

    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    hummer.drive(11)
    print("${:.2f}".format(hummer.get_fare()))



main()