"""Tests for Class Taxi."""

from prac_08.taxi import Taxi

# 1 - Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

new_taxi = Taxi("Prius 1", 100, 1.23)
print(new_taxi)

# 2 - Drive the taxi 40km
new_taxi.drive(40)
print(new_taxi)

# 3 - Print the taxi's details and the current fare

print(new_taxi)
print("name:", new_taxi.name)
print("fuel", new_taxi.fuel)
print("odometer", new_taxi.odometer)
print("fare distance", new_taxi.current_fare_distance)
print("fare $", new_taxi.price_per_km, "per/km")
print("current fare: $", new_taxi.get_fare())


