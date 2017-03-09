'''
Authors: Emily Lepert and Vicky McDermott
'''
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
		'''
		The integration class pulls everything together. 

		update_layout: monitors which question we're currently on and updates 
			the question child with the following question using info about the 
			current index and data_type.

		run_until_end: checks for a button change until the end of the questionnaire

		Attributes: data_type, index, counter, layout, question, interpret
		'''
		#initial data_type
		self.data_type = 'comma'

		# index of question in current data_type
		self.index = 1

		# keeps track of how many questions have been answered
		self.counter = 1

		self.layout = Layout(self.index,
							 Interpret([0.02777] * 36, 2, "No", "comma"),
							 self.data_type, Data('comma'))
		self.question = Question(self.index,
								 Interpret([0.02777] * 36, 2, "No", "comma"),
								 self.data_type, Data(self.data_type))
		self.interpret = Interpret([0.02777] * 36, 2, "No", "comma")
		


	def update_layout(self, new):
		'''
		Initiates updating layout based on current question and data_type
		'''
		# gets list of possible answers of current question
		answers = self.question.get_list_answers(self.question.get_fig()[1])

		# gets selected answer
		response = answers[new]

		# updates the map and ageline
		self.layout.update_visuals(self.index, response, self.data_type)

		self.index += 1
		# if the next question is a comma question
		if self.data_type == 'comma' and self.index < 11:
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1
		# if the next question is supposed to be the first earthquake question
		elif self.data_type == 'comma' and self.index == 11:
			self.data_type = 'earthquake'
			self.interpret = Interpret([0.02777] * 36, 0, "Not at all worried", self.data_type)
			self.index = 1
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1
		# if the next question is supposed to be an earthquake question
		elif self.data_type == 'earthquake' and self.index < 7:
			self.layout.change_layout(self.index, self.interpret, Data(self.data_type), self.data_type)
			self.counter += 1

		# update Question object with updated values
		self.question = Question(self.index, self.interpret, self.data_type, Data(self.data_type))

		self.run_until_end()

	def run_until_end(self):
		'''
		Sets up the layout and checks for a change in the radio group
		'''
		# sets up the intial layout
		if self.counter == 1:
			self.layout.get_layout()
	
		#anytime after the first cycle
		if self.counter < 16:
			Question.answer.on_click(self.update_layout)
		# after the last question
		elif self.counter == 16:
			# Writes out the highest probability location and age
			final_blurb = Div(text='You are most likely to be '+ self.layout.biggest_prob() + ' region.')
			new_layout = widgetbox(final_blurb)
			self.layout.final_layout(new_layout)


integrate = Integration()	
integrate.run_until_end()
