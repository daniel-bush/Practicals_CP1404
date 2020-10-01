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
        miles = float(self.root.ids.input_miles.text)
        kms = miles * KM_IN_MILE
        self.message = str(kms)

    def handle_increment(self, increment):
        current_miles = float(self.root.ids.input_miles.text)
        current_miles += increment
        self.root.ids.input_miles.text = str(current_miles).format()


MilesToKMsApp().run()