from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Daniel", "Colin", "Sandra", "Victoria"]


class DynamicLabelsApp(App):
    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create dynamic label"""
        for name in NAMES:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()

