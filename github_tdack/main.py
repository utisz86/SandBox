import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty

import RPi.GPIO as GPI

"""
Base class for a GPIO based button
"""
class GPIOButton(Button):
	pin = NumericProperty(None)
	direction = NumericProperty(None)
	pull_up_down = NumericProperty(None, allownone=True)
	value = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(GPIOButton, self).__init__(**kwargs)
        # Setup GPIO pin based on .kv properties
		if self.pin is None:
		    # pin not set, so don't do any configuring
			return
		# Below never gets executed as self.pin is always None in __init__()
		if self.direction == GPIO.OUT:
			print("setting up {}".format(self.pin))
			GPIO.setup(self.pin, self.direction, pull_up_down=self.pull_up_down)
		else:
			GPIO.setup(self.pin, self.direction)
		if self.value is not None:
			GPIO.output(self.pin, self.value)

""" Button that will toggle based on GPIO input """
class GPIOInputButton(GPIOButton):
	pass

""" Button that will change a GPIO output """
class GPIOPressButton(GPIOButton, Button):
	pass

class Monitor(Widget):
	def init_GPIO(self):
		# Set up GPIO
		GPIO.setmode(GPIO.BCM)

class MonitorApp(App):
	def build(self):
		monitor = Monitor()
		monitor.init_GPIO()
		return monitor

if __name__ == '__main__':
	MonitorApp().run()