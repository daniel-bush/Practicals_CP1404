"""Daniel Bush - CP1404. Convert miles to km program."""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

KM_IN_MILE = 1.60934


class MilesToKMsApp(App):
    """MilesTOKMsApp is a app using kivy to convert miles to kilometers."""
    message = StringProperty()

    def build(self):
        """Build the app from kivy file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Handle the conversion calculation when text is edited. Output to the label widget."""
        miles = self.get_correct_miles_input()
        kms = miles * KM_IN_MILE
        self.message = str(kms)

    def handle_increment(self, increment):
        """Handle the up/down button press. Update input_text widget with new value."""
        miles = self.get_correct_miles_input()
        miles += increment
        self.root.ids.input_miles.text = str(miles)

    def get_correct_miles_input(self):
        """Validate if value is a float and return value. Return 0.0 if value error."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesToKMsApp().run()