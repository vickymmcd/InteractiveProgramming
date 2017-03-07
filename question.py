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
	next_button= Button(label="Next", button_type="success")
	answer = RadioGroup(labels=['dfd', 'dfd'], active=0)
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
		

		self.question_type = data.get_question(self.index)
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
		self.question = Div(text=self.question_type)
		#calls the appropriate layout class based on the options
		if len(self.qa[self.index]) == 2:
			Question.answer = RadioGroup(labels=[self.qa[self.index][0], self.qa[self.index][1]])
			choices = widgetbox(self.question, Question.answer)
		elif len(self.qa[self.index]) == 5:
			Question.answer = RadioGroup(labels=[self.qa[self.index][0],self.qa[self.index][1],self.qa[self.index][2], self.qa[self.index][3], self.qa[self.index][4]], active=0)
			choices = widgetbox(self.question,Question.answer)

		return(choices)

	def get_button(self):
		button = vform(Question.next_button)
		return(button)


class Two_choices():
	"""
	Class for questions with 2 possible answers
	"""
	def __init__(self, question, answers):
		self.question = question
		self.answers = answers

	def layout(self):
		"""
		Specifies the layout
		"""
		
		answers = RadioGroup(labels=[self.answers[0], self.answers[1]], active=0)
		widget = widgetbox(question,answers, self.next_button)
		return(widget)

class Five_choices():
	"""
	Class for questions with 5 possible answers
	"""
	def __init__(self, question, answers):
		self.question = question
		self.answers = answers

	def layout(self):
		"""
		Specifies the layout
		"""
		self.answer = RadioGroup(labels=[self.answers[0], self.answers[1],self.answers[2], self.answers[3], self.answers[4]], active=0)
		widget = widgetbox(self.question,self.answer, self.next_button)
		return(widget)

"""
data = Data('comma')
prior = [0.02777] * 36
newdictionary1 = Interpret(prior, 2, "No", "comma")
question = Question(1, newdictionary1, "comma")
widget = question.return_layout()
output_file('layout1.html')
show(widget)
"""
