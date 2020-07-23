from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock


class MyButton(Button):
    def __init__(self):
        self.current_touch = None

    def on_touch_down(self, touch):
        if self.current_touch is not None:
            Clock.unschedule(self.scheduled_func)
            self.on_double_press()
            self.current_touch = None
        else:
            self.current_touch = touch
            Clock.schedule_once(self.on_single_press, 0.1)

    def on_double_press(self):
        print("Two click")

    def on_single_press(self):
        print("Single click")

class MyApp(App):
    def build(self):
        button = MyButton(text='Hello World')
        return button

if __name__ == '__main__':
    MyApp().run()