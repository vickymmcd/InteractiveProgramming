"""
Integration of all components to make an awesome thing!!!!
"""
from ageline import AgeLine
from map import Map
from question import Question
from interpret import Interpret
from data import Data
from layout import Layout
from scaleline import ScaleLine
from bokeh.models import Button
from bokeh.models.widgets import Toggle

class Integration():
	def __init__(self):
		self.layout = Layout(1, Interpret(Data('comma'), [0.02777] * 36, 2, "No", "comma"), 'comma', Data('comma'))

	def update_layout(self):
		print('you clikced this button')
		Question.next_button = Toggle(label="Next", button_type="success")
		self.layout.show_layout()


	def define_layout(self):
		self.layout.show_layout()
		while True:
			Question.next_button.on_click(self.update_layout())
			

	

integrate = Integration()
integrate.define_layout()
