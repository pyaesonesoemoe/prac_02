from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names={"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title= "Dynamic labels"
        self.root= Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label= Label(text=name)
            temp_label.color= NEW_COLOUR
            self.root.ids.main_box.add_widget(temp_label)

DynamicLabelsApp().run()