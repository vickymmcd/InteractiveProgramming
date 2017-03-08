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
	answer = RadioGroup(labels=['dfd', 'dfd'], active=0)
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
		#for the sake of simplicity and time, writing the questions down saves time
		#but in the long term we would have to implement an automatic way of doing this
		#list of comma questions
		self.comma_questions = ["In your opinion, which sentence is more gramatically correct?",
			"Have you heard of the serial (or Oxford) comma?",
			"How much, if at all, do you care about the use (or lack thereof) of the serial (or Oxford) comma in grammar?",
			"How would you write the following sentence?",
			"When faced with using the word "'data'", have you ever spent time considering if the word was a singular or plural noun?",
			"How much, if at all, do you care about the debate over the use of the word "'data'" as a singluar or plural noun?",
			"In your opinion, how important or unimportant is proper use of grammar?",
			"What is your gender?",
			"What is your household income?",
			"What is your highest level of education?"]
		#list of earthquake questions
		self.earthquake_questions = ["In general, how worried are you about earthquakes?",
			"How worried are you about the Big One, a massive, catastrophic earthquake?",
			"Do you think the "'Big One'" will occur in your lifetime?",
			"Have you ever experienced an earthquake?",
			"Have you or anyone in your household taken any precautions for an earthquake (packed an earthquake survival kit, prepared an evacuation plan, etc.)?",
			"How familiar are you with the San Andreas Fault line?",
			"How familiar are you with the Yellowstone Supervolcano?"]

	def get_fig(self):
		"""
		Chooses between a 2 answer options question or 5 answer options question
		"""
		#uses the data_type info to select the appropriate questions list
		"""
		if self.data_type == "comma":
			questions = self.comma_questions
		elif self.data_type == "earthquake":
			questions = self.earthquake_questions
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
		elif len(self.qa[self.index]) == 5:
			Question.answer = RadioGroup(labels=self.get_list_answers(5))
			choices = widgetbox(Question.question,Question.answer)
			items = 5

		return([choices, items])
	'''
	def get_button(self):
		button = vform(Question.next_button)
		return(button)
	'''
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
