from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty

from kivy.graphics import Color
from kivy.graphics import Rectangle


class KivySpinboxApp(App):
    
    def build(self):
        g = BoxLayout()
        spin = KivySpinbox()
        g.add_widget(spin)
        return g

class KivySpinbox(Widget):
    def __init__(self,**kwargs):
        self.value = 0
        self.cols=2
        self.rows=1
        super(KivySpinbox, self).__init__(**kwargs)

        root = GridLayout(cols=2,rows=1)
        root.add_widget(Label(text="[color=000000]{0}".format(self.value), font_size='20sp', markup = True))
        
        up_down_btn = BoxLayout(orientation="vertical")
        root.add_widget(up_down_btn)

        up_button = Button(text = "[color=000000]+", font_size='20sp', markup = True)
        down_button = Button(text = "[color=000000]-", font_size='20sp', markup = True)

        up_button.bind(on_press=self.add_value)
        down_button.bind(on_press=self.add_value)


        up_down_btn.add_widget(up_button)
        up_down_btn.add_widget(down_button)

        self.add_widget(root)

        with self.canvas.before:
            Color(.9,.9,1)  
            self.Backgroud = Rectangle(pos=self.pos,size=self.size)        

        self.size = self.size
        self.pos = self.pos
    
    def add_value(self):
        self.value += 1

    def minus_value(self):
        if self.value > 0:
            self.value -= 1
        
class StoryWidget(GridLayout):
    def __init__(self,**kwargs):
        self.cols=1
        self.rows=1
        super(StoryWidget, self).__init__(**kwargs)
        topLayout=BoxLayout(orientation = "vertical")
        topLayout.add_widget(Button(text="first"))
        topLayout.add_widget(Button(text="second"))
        self.add_widget(topLayout)

        with self.canvas.before:
            Color(.9,.9,1)  
            self.Backgroud = Rectangle(pos=self.pos,size=self.size)

        self.bind(pos=self.repaint,size=self.repaint)
        self.bind(pos=self.resize,size=self.resize)




if __name__ == "__main__":
    KivySpinboxApp().run()
