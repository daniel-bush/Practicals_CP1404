from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_IN_KM = 1.60934

class MilesToKMsApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        miles = int(self.root.ids.input_miles.text)
        kms = miles * MILES_IN_KM
        self.message = str(kms)


MilesToKMsApp().run()