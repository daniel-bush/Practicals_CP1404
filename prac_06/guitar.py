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

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year


def test_code():
    tester = Guitar("Tester", 2000, 150)
    print(tester)
    print(tester.get_age())


if __name__ == "__main__":
    test_code()
