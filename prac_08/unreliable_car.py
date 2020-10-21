"""Class for ynreliable car."""

from prac_06.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initalise a Unreliable Car instance based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
