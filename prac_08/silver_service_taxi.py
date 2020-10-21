"""Silver Service taxi class."""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Reoresent a silver service taxi."""

    def __init__(self, name, fuel, fanciness):
        """Initalise as SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{}, fanciness {}".format(super().__str__(), self.fanciness)