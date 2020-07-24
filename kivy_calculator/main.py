from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class SmartPlateApp(App):

    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        button_grid = GridLayout(cols=7, size_hint_y=10)

        for symbol in range(70):
            button_grid.add_widget(Button(text="0"))        


        def print_button_text1(instance):
            instance.text = str(int(instance.text) - 1)

        
        def print_button_text2(instance):
            instance.text = str(int(instance.text) + 2)
            

        for button in button_grid.children:  # note use of the
                                             # `children` property
            button.bind(on_press=print_button_text1)
            button.bind(on_release =print_button_text2)
            


        root_widget.add_widget(button_grid)

        return root_widget



if __name__ == '__main__':
    SmartPlateApp().run()