"""
This is the question class
"""
from interpret import Interpret
from data import Data
from bokeh.io import output_file, show, vform
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioGroup
from bokeh.models.widgets import Div
from bokeh.models.widgets import Button

class Question():
	"""
	Class creates the layout for each question
	"""
	#next_button= Button(label="Next", button_type="success")
	answer = RadioGroup(labels=['dfd', 'dfd'])
	question = Div(text='dkfjd')
	def __init__(self,index, interpret, data_type, data):
		#differentiates between earthquake and comma
		self.data_type = data_type
		#Interpret class reference
		self.interpret = interpret
		#question number in either earthquake or comma
		self.index = index
		#dictionary of questions and answers from the Interpret class
		self.qa = self.interpret.dictionary_of_qa()

		#self.next_button = Toggle(label="Next", button_type="success")
		self.question = Div(text="example")
		

		self.question_typed_out = data.get_question(self.index)

	def get_fig(self):
		"""
		Chooses between a 2 answer options question or 5 answer options question
		"""
		Question.question = Div(text=self.question_typed_out)
		#calls the appropriate layout class based on the options
		if len(self.qa[self.index]) == 2:
			Question.answer = RadioGroup(labels=self.get_list_answers(2))
			choices = widgetbox(Question.question, Question.answer)
			items = 2
		elif len(self.qa[self.index]) == 4:
			Question.answer = RadioGroup(labels=self.get_list_answers(4))
			choices = widgetbox(Question.question,Question.answer)
			items = 4
		elif len(self.qa[self.index]) == 3:
			Question.answer = RadioGroup(labels=self.get_list_answers(3))
			choices = widgetbox(Question.question,Question.answer)
			items = 3
		elif len(self.qa[self.index]) == 5:
			Question.answer = RadioGroup(labels=self.get_list_answers(5))
			choices = widgetbox(Question.question,Question.answer)
			items = 5

		return([choices, items])

	def get_list_answers(self, items):
		list_answers = []
		for i in range(items):
			list_answers.append(self.interpret.key_formatting(self.qa[self.index][i]))
		return(list_answers)




"""
data = Data('comma')
prior = [0.02777] * 36
newdictionary1 = Interpret(prior, 2, "No", "comma")
question = Question(1, newdictionary1, "comma")
widget = question.return_layout()
output_file('layout1.html')
show(widget)
"""
