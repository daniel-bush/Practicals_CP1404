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
        """Calculates the age of guitar."""
        current_year = datetime.now().year  # looks up the current year from the system clock.
        return current_year - self.year

    def is_vintage(self):
        """Calculates if guitar is vintage - is true if age is greater or equal to 50 years old."""
        current_age = self.get_age()
        if current_age >= 50:
            return True
        else:
            return False


def test_code():
    tester = Guitar("Tester", 2000, 150)
    print(tester)
    print(tester.get_age())


if __name__ == "__main__":
    test_code()
