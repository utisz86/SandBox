from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty


class GuiApp(App):
    
    def build(self):
        g = Gui()
        for i in range(24):
            g.grid.add_widget(Button(text='test'))
        return g

class Gui(BoxLayout):
    grid = ObjectProperty(None)


if __name__ == "__main__":
    GuiApp().run()
