"""Silver Service taxi class."""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise as SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the silver service trip."""
        return super().get_fare() + self.flagfall

