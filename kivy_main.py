import kivy

from kivy.app import App
from kivy.uix.label import Label

class Mylabel(Label):
    def on_touch_down(self, touch):
        if touch.is_double_tap:
            print("Two click")
                    
        if touch.is_touch:
            print("One click")


class MyApp(App):

    def build(self):
        return Mylabel(text='0')


if __name__ == '__main__':
    MyApp().run()