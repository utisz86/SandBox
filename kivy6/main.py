from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string(
'''
<FirstWidget>:      
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 10
    Button:
        text: 'change to form 2'
        on_release: root.ChangeWidget('form2')

<SecondWidget>:
    TextInput:
    BubbleButton:
        text: 'change to form 1'
        on_release: root.ChangeWidget('form1')
''')

class UserInterface():
    __WidgetDictionary = {}
    __RootWidget = None

    def __init__(self, inRootWidget):
        self.__RootWidget = inRootWidget # Keep track of our root
        # Generate two forms to be swapped in/out
        self.__WidgetDictionary["form1"] = FirstWidget()
        self.__WidgetDictionary["form1"].SetUIReference(self)

        self.__WidgetDictionary["form2"] = SecondWidget()
        self.__WidgetDictionary["form2"].SetUIReference(self)
        self.ChangeWidget("form1")

    def ChangeWidget(self, inWidgetName):
         # Clear out the widgets
        self.__RootWidget.clear_widgets()
         # Add our new widget
        self.__RootWidget.add_widget(self.__WidgetDictionary[inWidgetName])


class FirstWidget(BoxLayout):
    __UserInterfaceReference = None

    def SetUIReference(self, inUserInterface):
        self.__UserInterfaceReference = inUserInterface

    def ChangeWidget(self, inWidgetName):
        self.__UserInterfaceReference.ChangeWidget(inWidgetName)

class SecondWidget(BoxLayout):
    __UserInterfaceReference = None

    def SetUIReference(self, inUserInterface):
        self.__UserInterfaceReference = inUserInterface

    def ChangeWidget(self, inWidgetName):
        self.__UserInterfaceReference.ChangeWidget(inWidgetName)


class MyApp(App):

    def build(self):
        rootForm = BoxLayout()
        ui = UserInterface(rootForm)
        return rootForm


if __name__ == '__main__':
    MyApp().run()