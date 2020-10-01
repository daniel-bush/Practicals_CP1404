from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

KM_IN_MILE = 1.60934


class MilesToKMsApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        miles = self.get_correct_miles_input()
        kms = miles * KM_IN_MILE
        self.message = str(kms)

    def handle_increment(self, increment):
        miles = self.get_correct_miles_input()
        miles += increment
        self.root.ids.input_miles.text = str(miles).format()

    def get_correct_miles_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesToKMsApp().run()