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
		self.data_type = 'comma'
		self.layout = Layout(1, Interpret([0.02777] * 36, 2, "No", "comma"), self.data_type, Data('comma'), [.25, .25, .25, .25], [0, .11, .11, .11, .11, .11, .11, .11, .11, .11])

	def update_layout(self, new):
		answers = self.layout.show_list_answers()[0]
		question_index = self.layout.show_list_answers()[1]
		response = answers[new]
		print(response, question_index)

	def define_layout(self):
		self.layout.get_layout()
		self.layout.show_layout()
		Question.answer.on_click(self.update_layout)
		
		

integrate = Integration()
integrate.define_layout()

