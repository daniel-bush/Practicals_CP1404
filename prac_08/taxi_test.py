"""Tests for Class Taxi."""

from prac_08.taxi import Taxi

# 1 - Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

new_taxi = Taxi("Prius 1", 100, 1.23)
print(new_taxi)

# 2 - Drive the taxi 40km
new_taxi.drive(40)
print(new_taxi)

