"""Class for ynreliable car."""

from prac_06.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initalise a Unreliable Car instance based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Returns string from Parent Class pluss reliability."""
        return "{}, reliability: {}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        """Drive the car only if reliable."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
