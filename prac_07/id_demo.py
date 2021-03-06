import random
from kivy.app import App
from kivy.lang import Builder


class IDDemo(App):
    """IDDemo is an app that asks for a name and greats them."""
    def build(self):
        self.title = "Demoing the id attribute"
        self.root = Builder.load_file('id_demo.kv')
        return self.root

    def handle_pressed(self):
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
        else:
            self.root.ids.my_label.text = "stop that!!"


# Create and start the App running
IDDemo().run()
