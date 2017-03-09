"""
Authors: Emily Lepert and Vicky McDermott
"""
from interpret import Interpret
from data import Data
from bokeh.io import output_file, show, vform
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioGroup, Div, Button

class Question():
	
	# placeholder radiogroup variable so it can be modified later
	answer = RadioGroup(labels=['dfd', 'dfd'])

	def __init__(self,index, interpret, data_type, data):
		'''
		Determines layout of the question child

		Attributes: data_type, interpret, index, qa, question_typed_out, question
		'''
		#differentiates between earthquake and comma
		self.data_type = data_type
		#Interpret class reference
		self.interpret = interpret
		#question number in either earthquake or comma
		self.index = index
		#dictionary of questions and answers from the Interpret class
		self.qa = self.interpret.dictionary_of_qa()

		# Written out question
		self.question_typed_out = data.get_question(self.index)

		# Question text div
		self.question = Div(text=self.question_typed_out)

	def get_fig(self):
		'''
		Creates the question and answer widget
		'''

		#creates a radio group with the appropriate answer options
		length = len(self.qa[self.index])
		Question.answer = RadioGroup(labels=self.get_list_answers(length))
		choices = widgetbox(self.question, Question.answer)
		items = length

		return([choices, items])

	def get_list_answers(self, items):
		'''
		Outputs the list of answers for the question
		'''
		list_answers = []
		for i in range(items):
			list_answers.append(self.interpret.key_formatting(self.qa[self.index][i]))
		return(list_answers)

