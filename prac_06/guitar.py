"""CP1404 Guitars! Exercise."""

from datetime import datetime


class Guitar:
    """Class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)



