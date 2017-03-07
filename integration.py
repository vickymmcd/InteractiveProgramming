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
from bokeh.plotting import figure, curdoc

class Integration():
	def __init__(self):
		self.layout = Layout(1, Interpret([0.02777] * 36, 2, "No", "comma"), 'comma', Data('comma'), [.25, .25, .25, .25], [0, .11, .11, .11, .11, .11, .11, .11, .11, .11])

	def update_layout(self):
		print('dfdf')
		#Question.next_button = Button(label="Next", button_type="success")
		#counter += 1
		#print(counter)
		#if counter > 0:
			#return('')
		
		#self.layout.show_layout()


	def define_layout(self):
		
		Question.next_button.on_click(self.update_layout())

			

	

integrate = Integration()
integrate.define_layout()
