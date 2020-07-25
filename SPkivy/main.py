# Kivy moduls
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.lang import Builder

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

# Time modul
import datetime
import pickle

# Own modul for data
from WeekClass import WeekClass
from setup_weekdata import setup_weekdata

# Color variables
red = [1, 0, 0, 1]  
green = [0, 1, 0, 1]

# Pop up button
Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .6, .6
    auto_dismiss: False
    title: 'Instruction'
    Button:
        text: "[b][color=0000ff]Zöldség/Gyümölcs[/color][/b]: 1 adag = 10 dkg friss, párolt vagy főtt, idényjellegű zöldség vagy gyümölcs (pl. 1 közepes paprika, paradicsom,  1 közepes alma vagy narancs) vagy 1 kis tányér saláta vagy 1 kis pohárnyi bogyós gyümölcs. Fogyassz száraz hüvelyeseket (pl. babot, lencsét, csicseriborsót, szóját) levesek, főzelékek, saláták, krémek részeként.[b][color=0000ff]Gabona:[/color][/b] 1 adag = 1 db péksütemény (pl. kifli vagy zsemle) vagy 1 közepes szelet kenyér/kalács vagy 12 evőkanál (20 dkg:3) főtt tészta/rizs vagy 3 evőkanál gabonapehely/müzli [b][color=0000ff]Hús/Tej:[/color][/b] 1 adag = 2 dl tej/joghurt/kefír vagy 5 dkg túró vagy 3 dkg sajt vagy 1 tenyérnyi szelet (10 dkg) hús vagy 1 szelet (15 dkg) hal vagy 3-4 szelet (5 dkg) felvágott vagy 1 db tojás [b][color=0000ff]Magvak:[/color][/b] pl. diót, mandulát, mogyorót, tökmagot, napraforgómagot."
        on_press: pop.dismiss()
        text_size : self.width, None
        height: self.texture_size[1]
        markup:True
''')


class SimplePopup(Popup):
    pass


class SimpleButton(Button):
    # Import or create week data
    weekdata = setup_weekdata()
    # This week data
    my_date = datetime.date.today()
    year, week_num, day_of_week = my_date.isocalendar()

    day_text = "{1}: {0} week".format(week_num, year)
    text = day_text
    def fire_popup(self):
        pops=SimplePopup()
        pops.open()

class SmartPlateApp(App):
    # Import or create week data
    weekdata = setup_weekdata()
    # This week data
    my_date = datetime.date.today()
    year, week_num, day_of_week = my_date.isocalendar()

    spinboxs = []
    label_minmax = []

    def spinbox_minmax(self):
        # Refress week Min_Max colour
        for (j, food) in enumerate(self.weekdata.foodEvents):
            # Sum up all data es
            sum_event = sum(int(i) for i in self.weekdata.data[j])
            # compare min and max,
            # if exceed change the color
            if sum_event >= self.weekdata.weekMin[j] and sum_event <= self.weekdata.weekMax[j]:
                self.label_minmax[j*2].background_color = green
                self.label_minmax[j*2+1].background_color = green
            else:
                self.label_minmax[j*2].background_color = red
                self.label_minmax[j*2+1].background_color = red    
            
            # Refress spinbox bg colour
            # Check if day value larger dan daily max
            # if yes, change colour
            index_max = 0
            j = 6
            for (i, spinbox) in enumerate(self.spinboxs):
                if int(spinbox.text) > self.weekdata.dayMax[index_max] or int(spinbox.text) < 0:
                    spinbox.background_color = red
                else:
                    spinbox.background_color = green
                
                if i == j:
                    index_max += 1
                    j += 7


    def build(self):
        
        # Function for down-up
        def add_value(instance):
            # Change the data
            instance.text = str(int(instance.text) + 2)
            print("add{0}".format(instance.text))
            # Refresh the data from buttons to weekdata
            spin_index = 0
            
            for (j, event) in enumerate(self.weekdata.foodEvents):
                for (i, day) in enumerate(self.weekdata.weekDays):
                    self.weekdata.data[j][i] = self.spinboxs[spin_index].text
                    spin_index += 1
            # Save the data to the original file
            with open("week"+str(self.year)+str(self.week_num)+"_data.pkl", 'wb') as output:
                pickle.dump(self.weekdata, output, pickle.HIGHEST_PROTOCOL)

            # Refress week Min_Max colour     
            # Refress spinbox bg colour
            self.spinbox_minmax()


        def minus_value(instance):
            # Change the data
            instance.text = str(int(instance.text) - 1)
            print("min{0}".format(instance.text))
            # Refresh the data from buttons to weekdata
            spin_index = 0
            for (j, event) in enumerate(self.weekdata.foodEvents):
                for (i, day) in enumerate(self.weekdata.weekDays):
                    self.weekdata.data[j][i] = self.spinboxs[spin_index].text
                    spin_index += 1            
            # Save the data to the original file
            with open("week"+str(self.year)+str(self.week_num)+"_data.pkl", 'wb') as output:
                pickle.dump(self.weekdata, output, pickle.HIGHEST_PROTOCOL)       

            # Refress week Min_Max colour     
            # Refress spinbox bg colour   
            self.spinbox_minmax()

        # Basic frame
        root_widget = BoxLayout(orientation='horizontal')
        
      
        # Week foods col
        # Basic grid framework first column
        weekcol_grid = GridLayout(cols=1, rows= len(self.weekdata.foodEvents) + 1, size_hint_y=2, width=100, size_hint=(None, 1))
        
        # Add labels
        # First popup button
        weekcol_grid.add_widget(SimpleButton())
        # Rest elements
        for (j, event) in enumerate(self.weekdata.foodEvents):
            weekcol_grid.add_widget(Label(text=event))

        # Spinbox-Buttons
        # Basic grid
        weekbutton_grid = GridLayout(cols=len(self.weekdata.weekDays), rows= len(self.weekdata.foodEvents)+1, width=600, size_hint=(None, 1))
        # Spinboxes
        for (i, day) in enumerate(self.weekdata.weekDays):
            weekbutton_grid.add_widget(Label(text=day))        

        for (j, event) in enumerate(self.weekdata.foodEvents):
            for (i, day) in enumerate(self.weekdata.weekDays):
                var = str(self.weekdata.data[j][i])
                new_button = Button(text=var)
                weekbutton_grid.add_widget(new_button)
                # Add to list
                self.spinboxs.append(new_button)

        # Add functions
        for button in weekbutton_grid.children:
            button.bind(on_press=minus_value)
            button.bind(on_release =add_value)

        # Min-max labels
        # Basic grid
        weekminmax_grid = GridLayout(cols=2, rows= len(self.weekdata.foodEvents)+1, size_hint_y=2, width=100, size_hint=(None, 1))

        weekminmax_grid.add_widget(Label(text="Min" ))
        weekminmax_grid.add_widget(Label(text="Max" ) )

        # Add labels
        for (j, event) in enumerate(self.weekdata.foodEvents):
            new_minmax = Button(text=str(self.weekdata.weekMin[j]))
            weekminmax_grid.add_widget(new_minmax)
            self.label_minmax.append(new_minmax)

            new_minmax = Button(text=str(self.weekdata.weekMax[j]))
            weekminmax_grid.add_widget(new_minmax)
            self.label_minmax.append(new_minmax)
            


        # Add widget to root_widget
        
        root_widget.add_widget(weekcol_grid)
        root_widget.add_widget(weekbutton_grid)
        root_widget.add_widget(weekminmax_grid)
      
        self.spinbox_minmax()

        return root_widget



if __name__ == "__main__":
    SmartPlateApp().run()