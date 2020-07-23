from kivy.app import App

from kivy.uix.label import Label


class DoubleClickableLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.register_event_type('on_double_press')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return Label.on_touch_down(self, touch)

    def on_double_press(self, *args):
        pass


class MyApp(App):
    def build(self):
        label = DoubleClickableLabel(text='Hello world', on_double_press=self.callback)
        return label

    def callback(self, *args):
        print("double clicked", args[0])


if __name__ == '__main__':
    MyApp().run()