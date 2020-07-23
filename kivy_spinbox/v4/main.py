from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from kivy.graphics import Color
from kivy.graphics import Rectangle


class KivySpinboxWindowApp(App):
    
    def build(self):
        g = GridLayout(rows=12, cols=10)
        for i in range(10*12):
            g.add_widget(KivySpinbox())
        return g


class KivySpinbox(Widget):
    
    # Give data from python to kivy
    spin_value = NumericProperty(0)
    

    def value_add(self):
        self.spin_value += 1

    def value_minus(self):
        if self.spin_value > 0:
            self.spin_value -= 1

        

if __name__ == "__main__":
    KivySpinboxWindowApp().run()
