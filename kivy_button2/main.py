import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

class MyButton(Button):
    
    spin_value = NumericProperty(0)

    def on_touch_down(self, touch):
        if touch.is_double_tap and touch.double_tap_time < 1500:
            if self.spin_value >= 2:
                self.spin_value -= 2
            else:
                self.spin_value -= 1
            print("Two click{0}".format(self.spin_value))
        else:
            self.spin_value += 1
            print("One click{0}".format(self.spin_value))


class MyApp(App):

    def build(self):
        return MyButton()


if __name__ == '__main__':
    MyApp().run()