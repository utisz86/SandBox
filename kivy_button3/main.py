import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

class MyButton(Button):
    spin_value = StringProperty(0)

    def on_touch_down(self, touch):
        self.spin_value = "2"
        

class MyApp(App):

    def build(self):
        return MyButton(text='0')


if __name__ == '__main__':
    MyApp().run()