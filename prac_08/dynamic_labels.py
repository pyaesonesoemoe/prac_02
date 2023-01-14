from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super.().__init__(**kwargs)
        self.name={"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title= "Dynamic labels"
        self.root= Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            self.create_widgets(name)

        return self.root

    def create_widgets(self, name):
        button= Button(text=name)
        self.root.ids.main.box.add_widget(button)