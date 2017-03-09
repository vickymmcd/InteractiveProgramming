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
from bokeh.models.widgets import Toggle, Div
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column, row, widgetbox


class Integration():

	def __init__(self):
		self.data_type = 'comma'
		self.index = 1
		self.layout = Layout(self.index,
							 Interpret([0.02777] * 36, 2, "No", "comma"),
							 self.data_type, Data('comma'))
		self.question = Question(self.index,
								 Interpret([0.02777] * 36, 2, "No", "comma"),
								 self.data_type, Data(self.data_type))
		self.interpret = Interpret([0.02777] * 36, 2, "No", "comma")
		self.counter = 1


	def update_layout(self, new):
		answers = self.question.get_list_answers(self.question.get_fig()[1])
		response = answers[new]
		self.layout.update_stuff(self.index, response, self.data_type)
		print(Question.question.text, response)

		self.index += 1
		if self.data_type == 'comma' and self.index < 11:
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1
		elif self.data_type == 'comma' and self.index == 11:
			self.data_type = 'earthquake'
			self.interpret = Interpret([0.02777] * 36, 0, "Not at all worried", self.data_type)
			self.index = 1
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1
		elif self.data_type == 'earthquake' and self.index < 8:
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1

		self.question = Question(self.index, self.interpret, self.data_type, Data(self.data_type))
		self.run_until_end()


	def define_initial_layout(self):
		self.layout.get_layout()
		self.layout.show_layout()
		Question.answer.on_click(self.update_layout)

	def run_until_end(self):
		if self.counter < 17:
			print(self.counter)
			Question.answer.on_click(self.update_layout)
		else:
			final_blurb = Div(text='You are most likely to be '+ self.layout.biggest_prob() + ' region.')
			new_layout = widgetbox(final_blurb)
			self.layout.final_layout(new_layout)


integrate = Integration()
integrate.define_initial_layout()
