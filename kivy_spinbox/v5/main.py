from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, NumericProperty


class GuiApp(App):
    
    def build(self):
        g = Gui()
        for i in range(120):
            spin = KivySpinbox()
            g.grid.add_widget(spin)
        return g

class Gui(BoxLayout):
    grid = ObjectProperty(None)


class KivySpinbox(Widget):
    
    # Give data from python to kivy
    spin_value = NumericProperty(0)
    

    def value_add(self):
        self.spin_value += 1

    def value_minus(self):
        if self.spin_value > 0:
            self.spin_value -= 1    

if __name__ == "__main__":
    GuiApp().run()
